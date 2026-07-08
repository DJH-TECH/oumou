from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.urls import reverse

from .models import WpPosts
from .utils import format_post, fix_corrupted_text


NAV_CATEGORIES = [
    'Politique', 'Économie', 'International', 'Sport',
    'Culture', 'Technologie', 'Santé', 'Éducation',
]

HERO_FILTERS = [
    'Actualités', 'Politique', 'Économie', 'Business', 'Sport', 'Culture', 'Technologie',
]


def _get_published_posts(limit=None):
    qs = WpPosts.objects.filter(post_status='publish', post_type='post').order_by('-post_date')
    if limit:
        qs = qs[:limit]
    return [format_post(post) for post in qs]


def _get_hero_slide_posts(limit=4):
    posts = _get_published_posts(30)
    with_images = [p for p in posts if p['image_url']]
    without_images = [p for p in posts if not p['image_url']]
    return (with_images + without_images)[:limit]


def _build_hero_slides(posts):
    fallback_image = static('siteweb/images/hero-sunset.png')
    slides = []

    for post in posts:
        slides.append({
            'id': post['id'],
            'title': post['title'],
            'excerpt': post['excerpt'],
            'category': post['category'],
            'url': reverse('siteweb:post_detail', args=[post['id']]),
            'image': post['image_url'] or fallback_image,
        })

    if not slides:
        slides.append({
            'id': None,
            'title': "Le média qui raconte l'Afrique autrement.",
            'excerpt': (
                "Toute l'actualité africaine en temps réel : politique, économie, "
                "innovation, sport, culture, santé et éducation."
            ),
            'category': 'À LA UNE',
            'url': reverse('siteweb:post_list'),
            'image': fallback_image,
        })

    return slides


def home(request):
    breaking_posts = _get_published_posts(5)
    hero_slides = _build_hero_slides(_get_hero_slide_posts(4))
    published_count = WpPosts.objects.filter(post_status='publish', post_type='post').count()
    return render(request, 'siteweb/index.html', {
        'nav_categories': NAV_CATEGORIES,
        'hero_filters': HERO_FILTERS,
        'breaking_posts': breaking_posts,
        'hero_slides': hero_slides,
        'published_count': published_count,
    })


def posts_list(request):
    query = request.GET.get('q', '').strip()
    qs = WpPosts.objects.filter(post_status='publish', post_type='post')
    if query:
        qs = qs.filter(Q(post_title__icontains=query) | Q(post_content__icontains=query))
    posts = [format_post(post) for post in qs.order_by('-post_date')[:20]]
    return render(request, 'siteweb/posts_list.html', {
        'posts': posts,
        'nav_categories': NAV_CATEGORIES,
        'search_query': query,
    })


def post_detail(request, post_id):
    post = get_object_or_404(WpPosts, pk=post_id, post_status='publish')
    formatted = format_post(post)
    return render(request, 'siteweb/post_detail.html', {
        'post': post,
        'formatted': formatted,
        'fixed_content': fix_corrupted_text(post.post_content),
        'nav_categories': NAV_CATEGORIES,
    })
