(function () {
    'use strict';

    const SLIDE_DURATION = 6000;

    function pad(num) {
        return String(num).padStart(2, '0');
    }

    function initHeroSlider() {
        const section = document.getElementById('hero-section');
        const dataEl = document.getElementById('hero-slides-data');
        if (!section || !dataEl) return;

        let slides;
        try {
            slides = JSON.parse(dataEl.textContent);
        } catch (err) {
            return;
        }
        if (!slides.length) return;

        section.style.setProperty('--slide-duration', SLIDE_DURATION + 'ms');

        const bgImages = section.querySelectorAll('.hero-section__bg-img');
        const heroContent = section.querySelector('.hero-content');
        const categoryEl = section.querySelector('[data-hero-category]');
        const titleEl = section.querySelector('[data-hero-title]');
        const excerptEl = section.querySelector('[data-hero-excerpt]');
        const ctaEl = section.querySelector('[data-hero-cta]');
        const counterEl = section.querySelector('[data-slide-counter]');
        const progressEl = section.querySelector('[data-slide-progress]');
        const prevBtn = section.querySelector('[data-slide-prev]');
        const nextBtn = section.querySelector('[data-slide-next]');

        let current = 0;
        let activeBg = 0;
        let timer = null;
        let progressFrame = null;
        let progressStart = 0;

        function stopProgress() {
            if (progressFrame) {
                cancelAnimationFrame(progressFrame);
                progressFrame = null;
            }
        }

        function startProgress() {
            stopProgress();
            if (!progressEl) return;
            progressEl.style.width = '0%';
            progressStart = performance.now();

            function tick(now) {
                const elapsed = now - progressStart;
                const percent = Math.min((elapsed / SLIDE_DURATION) * 100, 100);
                progressEl.style.width = percent + '%';
                if (percent < 100) {
                    progressFrame = requestAnimationFrame(tick);
                }
            }

            progressFrame = requestAnimationFrame(tick);
        }

        function updateCounter() {
            if (counterEl) {
                counterEl.textContent = pad(current + 1) + ' / ' + pad(slides.length);
            }
        }

        function setContent(slide) {
            if (categoryEl) categoryEl.textContent = slide.category;
            if (titleEl) {
                titleEl.innerHTML = slide.title + '<span class="hero-dot">.</span>';
            }
            if (excerptEl) excerptEl.textContent = slide.excerpt;
            if (ctaEl) {
                ctaEl.href = slide.url;
                ctaEl.textContent = slide.id ? "Lire l'article →" : 'Découvrir les actualités →';
            }
        }

        const fallbackImage = section.dataset.fallbackImage || '';

        function bindImageFallback(img) {
            img.onerror = function () {
                if (fallbackImage && img.src !== fallbackImage) {
                    img.onerror = null;
                    img.src = fallbackImage;
                }
            };
        }

        bgImages.forEach(bindImageFallback);

        function setBackgroundImage(img, imageUrl) {
            bindImageFallback(img);
            img.src = imageUrl || fallbackImage;
        }

        function swapBackground(imageUrl) {
            if (bgImages.length < 2) return;
            const nextBg = 1 - activeBg;
            const incoming = bgImages[nextBg];
            const outgoing = bgImages[activeBg];

            outgoing.classList.remove('is-active');
            setBackgroundImage(incoming, imageUrl);
            incoming.classList.remove('is-active');
            void incoming.offsetWidth;
            incoming.classList.add('is-active');
            activeBg = nextBg;
        }

        function showSlide(index) {
            current = (index + slides.length) % slides.length;
            const slide = slides[current];

            if (heroContent) {
                heroContent.classList.add('is-animating');
                window.setTimeout(function () {
                    setContent(slide);
                    swapBackground(slide.image);
                    updateCounter();
                    heroContent.classList.remove('is-animating');
                }, 220);
            } else {
                setContent(slide);
                swapBackground(slide.image);
                updateCounter();
            }

            startProgress();
        }

        function nextSlide() {
            showSlide(current + 1);
            restartAutoplay();
        }

        function prevSlide() {
            showSlide(current - 1);
            restartAutoplay();
        }

        function restartAutoplay() {
            if (timer) clearInterval(timer);
            if (slides.length > 1) {
                timer = setInterval(nextSlide, SLIDE_DURATION);
            }
        }

        prevBtn?.addEventListener('click', prevSlide);
        nextBtn?.addEventListener('click', nextSlide);

        section.addEventListener('mouseenter', function () {
            if (timer) clearInterval(timer);
            stopProgress();
        });

        section.addEventListener('mouseleave', function () {
            restartAutoplay();
            startProgress();
        });

        updateCounter();
        startProgress();
        restartAutoplay();
    }

    document.addEventListener('DOMContentLoaded', initHeroSlider);
})();
