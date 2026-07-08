(function () {
    'use strict';

    const DEFAULT_LOCATION = { lat: 14.7167, lon: -17.4677, city: 'Dakar' };
    const GEO_CACHE_KEY = 'afrikapulse-weather-location';
    const GEO_CACHE_TTL = 30 * 60 * 1000;

    const WEATHER_ICONS = {
        sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>',
        cloud: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>',
        rain: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M16 13v8M8 13v8M12 15v8"/><path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"/></svg>',
        storm: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M19 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"/><path d="M13 11l-2 4h3l-2 4"/></svg>',
        fog: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M4 14h16M4 18h16M4 10h16"/><path d="M18 6h-1.26A8 8 0 1 0 4 10"/></svg>',
    };

    function weatherIconFor(code) {
        if (code === 0) return WEATHER_ICONS.sun;
        if (code <= 3) return WEATHER_ICONS.cloud;
        if (code <= 67 || code === 80 || code === 81) return WEATHER_ICONS.rain;
        if (code <= 99) return WEATHER_ICONS.storm;
        if (code === 45 || code === 48) return WEATHER_ICONS.fog;
        return WEATHER_ICONS.cloud;
    }

    function getCurrentPosition() {
        return new Promise(function (resolve, reject) {
            if (!navigator.geolocation) {
                reject(new Error('geolocation unavailable'));
                return;
            }
            navigator.geolocation.getCurrentPosition(resolve, reject, {
                enableHighAccuracy: false,
                timeout: 10000,
                maximumAge: 600000,
            });
        });
    }

    async function reverseGeocode(lat, lon) {
        const url = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude='
            + encodeURIComponent(lat) + '&longitude=' + encodeURIComponent(lon) + '&localityLanguage=fr';
        const response = await fetch(url);
        if (!response.ok) throw new Error('geocode unavailable');
        const data = await response.json();
        return data.city || data.locality || data.principalSubdivision || null;
    }

    async function getUserLocation() {
        try {
            const cached = sessionStorage.getItem(GEO_CACHE_KEY);
            if (cached) {
                const parsed = JSON.parse(cached);
                if (Date.now() - parsed.ts < GEO_CACHE_TTL) {
                    return parsed;
                }
            }
        } catch (err) {
            /* ignore invalid cache */
        }

        try {
            const position = await getCurrentPosition();
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            let city = DEFAULT_LOCATION.city;

            try {
                city = await reverseGeocode(lat, lon) || city;
            } catch (err) {
                /* keep fallback city name */
            }

            const location = { lat: lat, lon: lon, city: city, ts: Date.now() };
            sessionStorage.setItem(GEO_CACHE_KEY, JSON.stringify(location));
            return location;
        } catch (err) {
            return {
                lat: DEFAULT_LOCATION.lat,
                lon: DEFAULT_LOCATION.lon,
                city: DEFAULT_LOCATION.city,
                ts: Date.now(),
            };
        }
    }

    function updateWeatherWidgets(widgets, city, temp, icon) {
        widgets.forEach(function (widget) {
            const cityEl = widget.querySelector('[data-weather-city]');
            const tempEl = widget.querySelector('[data-weather-temp]');
            const iconEl = widget.querySelector('[data-weather-icon]');
            if (cityEl) cityEl.textContent = city;
            if (tempEl) tempEl.textContent = temp + '°C';
            if (iconEl) iconEl.innerHTML = icon;
            widget.title = 'Météo ' + city;
        });
    }

    async function loadWeather() {
        const widgets = document.querySelectorAll('[data-weather-widget]');
        if (!widgets.length) return;

        widgets.forEach(function (widget) {
            const cityEl = widget.querySelector('[data-weather-city]');
            if (cityEl) cityEl.textContent = '…';
        });

        const location = await getUserLocation();
        const weatherUrl = 'https://api.open-meteo.com/v1/forecast?latitude='
            + encodeURIComponent(location.lat) + '&longitude='
            + encodeURIComponent(location.lon)
            + '&current=temperature_2m,weather_code&timezone=auto';

        try {
            const response = await fetch(weatherUrl);
            if (!response.ok) throw new Error('weather unavailable');
            const data = await response.json();
            const temp = Math.round(data.current.temperature_2m);
            const icon = weatherIconFor(data.current.weather_code);
            updateWeatherWidgets(widgets, location.city, temp, icon);
        } catch (err) {
            updateWeatherWidgets(widgets, location.city, 29, WEATHER_ICONS.sun);
        }
    }

    function applyTheme(theme) {
        const isLight = theme === 'light';
        document.documentElement.classList.toggle('theme-light', isLight);
        localStorage.setItem('theme', isLight ? 'light' : 'dark');

        document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
            const moon = btn.querySelector('.theme-icon--moon');
            const sun = btn.querySelector('.theme-icon--sun');
            if (moon) moon.hidden = isLight;
            if (sun) sun.hidden = !isLight;
            btn.setAttribute('aria-label', isLight ? 'Activer le mode sombre' : 'Activer le mode clair');
        });
    }

    function initTheme() {
        const saved = localStorage.getItem('theme');
        applyTheme(saved === 'light' ? 'light' : 'dark');

        document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                const isLight = document.documentElement.classList.contains('theme-light');
                applyTheme(isLight ? 'dark' : 'light');
            });
        });
    }

    function initSearch() {
        const overlay = document.getElementById('search-overlay');
        if (!overlay) return;

        const input = overlay.querySelector('input[name="q"]');
        const openButtons = document.querySelectorAll('[data-search-open]');
        const closeButtons = overlay.querySelectorAll('[data-search-close]');

        function openSearch() {
            overlay.hidden = false;
            document.body.classList.add('search-open');
            openButtons.forEach(function (btn) { btn.setAttribute('aria-expanded', 'true'); });
            window.setTimeout(function () { input?.focus(); }, 50);
        }

        function closeSearch() {
            overlay.hidden = true;
            document.body.classList.remove('search-open');
            openButtons.forEach(function (btn) { btn.setAttribute('aria-expanded', 'false'); });
        }

        openButtons.forEach(function (btn) {
            btn.addEventListener('click', openSearch);
        });

        closeButtons.forEach(function (btn) {
            btn.addEventListener('click', closeSearch);
        });

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && !overlay.hidden) closeSearch();
        });
    }

    function initNavDrawer() {
        const drawer = document.getElementById('nav-drawer');
        if (!drawer) return;

        const openButtons = document.querySelectorAll('[data-nav-drawer-open]');
        const closeButtons = drawer.querySelectorAll('[data-nav-drawer-close]');

        function openDrawer() {
            drawer.hidden = false;
            document.body.classList.add('nav-drawer-open');
            openButtons.forEach(function (btn) { btn.setAttribute('aria-expanded', 'true'); });
        }

        function closeDrawer() {
            drawer.hidden = true;
            document.body.classList.remove('nav-drawer-open');
            openButtons.forEach(function (btn) { btn.setAttribute('aria-expanded', 'false'); });
        }

        openButtons.forEach(function (btn) {
            btn.addEventListener('click', openDrawer);
        });

        closeButtons.forEach(function (btn) {
            btn.addEventListener('click', closeDrawer);
        });

        drawer.querySelectorAll('.nav-drawer__links a').forEach(function (link) {
            link.addEventListener('click', closeDrawer);
        });

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && !drawer.hidden) closeDrawer();
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        loadWeather();
        initTheme();
        initSearch();
        initNavDrawer();
    });
})();
