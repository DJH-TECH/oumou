import re
from html import unescape

from django.utils import timezone
from django.utils.timesince import timesince

CATEGORY_KEYWORDS = {
    'Politique': ['ministre', 'gouvernement', 'élection', 'politique', 'conseil des ministres', 'communiqué'],
    'Économie': ['économie', 'banque', 'investissement', 'finance', 'bad', 'développement', 'ciment', 'emploi'],
    'International': ['union africaine', 'international', 'sahel', 'onu', 'diplomatie'],
    'Sport': ['sport', 'football', 'match', 'can ', 'coupe'],
    'Culture': ['culture', 'festival', 'musique', 'art'],
    'Technologie': ['technologie', 'digital', 'innovation', 'tech', 'numérique'],
    'Santé': ['santé', 'hôpital', 'médical', 'covid', 'épidémie'],
    'Éducation': ['éducation', 'école', 'université', 'formation'],
}

CATEGORY_COLORS = {
    'Politique': '#e63946',
    'Économie': '#f4a261',
    'International': '#e63946',
    'Sport': '#2a9d8f',
    'Culture': '#9b5de5',
    'Technologie': '#4361ee',
    'Santé': '#06d6a0',
    'Éducation': '#ffd166',
    'Actualités': '#e63946',
}

CATEGORY_SLUGS = {
    'Politique': 'politique',
    'Économie': 'economie',
    'International': 'international',
    'Sport': 'sport',
    'Culture': 'culture',
    'Technologie': 'technologie',
    'Santé': 'sante',
    'Éducation': 'education',
    'Actualités': 'default',
}


def fix_corrupted_text(text):
    """Répare les caractères accentués remplacés par ?? lors de l'export WordPress."""
    if not text or '?' not in text:
        return text

    fixes = [
        (r"l\?\?\?Emploi", "l'Emploi"),
        (r"l\?\?\?UEMOA", "l'UEMOA"),
        (r"l\?\?\?UMOA", "l'UMOA"),
        (r"l\?\?\?Union", "l'Union"),
        (r"l\?\?\?ann\?\?e", "l'année"),
        (r"l\?\?\?occasion", "l'occasion"),
        (r"d\?\?\?Ivoire", "d'Ivoire"),
        (r" \?\?\? ", " – "),
        (r" \?\? ", " à "),
        (r"deuxi\?\?me", "deuxième"),
        (r"premi\?\?re", "première"),
        (r"financi\?\?re", "financière"),
        (r"Probl\?\?matique", "Problématique"),
        (r"S\?\?n\?\?gal", "Sénégal"),
        (r"s\?\?n\?\?gal", "sénégal"),
        (r"c\?\?r\?\?monie", "cérémonie"),
        (r"g\?\?n\?\?ral", "général"),
        (r"coop\?\?ration", "coopération"),
        (r"p\?\?n\?\?tration", "pénétration"),
        (r"p\?\?trole", "pétrole"),
        (r"cha\?\?nes", "chaînes"),
        (r"pr\?\?voit", "prévoit"),
        (r"pr\?\?t", "prêt"),
        (r"B\?\?ninois", "Béninois"),
        (r"B\?\?nin", "Bénin"),
        (r"C\?\?te", "Côte"),
        (r"c\?\?te", "côte"),
        (r"ann\?\?e", "année"),
        (r"marqu\?\?", "marqué"),
        (r"chut\?\?", "chuté"),
        (r"d\?\?c\?\?s", "décès"),
        (r"D\?\?veloppement", "Développement"),
        (r"d\?\?veloppement", "développement"),
        (r"D\?\?velop", "Dévelop"),
        (r"d\?\?velop", "dévelop"),
        (r"R\?\?publi", "Républi"),
        (r"r\?\?alis", "réalis"),
        (r"r\?\?forme", "réforme"),
        (r"r\?\?sultat", "résultat"),
        (r"r\?\?vis\?\?", "révisé"),
        (r"s\?\?curis", "sécuris"),
        (r"d\?\?tourn", "détourn"),
        (r"d\?\?fi", "défi"),
        (r"g\?\?rant", "gérant"),
        (r"les \?\?tats", "les États"),
        (r"des \?\?tats", "des États"),
        (r"Cfa \?\? la", "Cfa à la"),
        (r"place \?\? un", "place à un"),
        (r"500 \?\? 15", "500 à 15"),
        (r"(\w)\?\?me\b", r"\1ème"),
        (r"(\w)\?\?re\b", r"\1ère"),
        (r"(\w)\?\?e\b", r"\1ée"),
        (r"(\w)\?\?t\b", r"\1êt"),
        (r"(\w)\?\?n", r"\1én"),
        (r"(\w)\?\?v", r"\1év"),
        (r"(\w)\?\?r", r"\1ér"),
        (r"(\w)\?\?l", r"\1él"),
        (r"(\w)\?\?m", r"\1ém"),
        (r"(\w)\?\?p", r"\1ép"),
        (r"(\w)\?\?f", r"\1éf"),
        (r"(\w)\?\?s\b", r"\1és"),
        (r"(\w)\?\?\b", r"\1é"),
        (r"\?\?(\w)", r"é\1"),
        (r"(\w)\?\?\?(\w)", r"\1'\2"),
    ]

    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text)

    return text


def strip_html(text):
    if not text:
        return ''
    text = re.sub(r'<[^>]+>', ' ', text)
    return fix_corrupted_text(unescape(re.sub(r'\s+', ' ', text)).strip())


def guess_category(title, content=''):
    text = f'{title} {strip_html(content)}'.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return category
    return 'Actualités'


def format_post(post):
    from .wp_images import get_post_image_url

    title = fix_corrupted_text(post.post_title)
    excerpt_source = fix_corrupted_text(post.post_excerpt) or strip_html(post.post_content)
    excerpt = excerpt_source[:180] + '…' if len(excerpt_source) > 180 else excerpt_source
    category = guess_category(title, post.post_content)
    post_date = post.post_date
    if timezone.is_naive(post_date):
        post_date = timezone.make_aware(post_date)
    return {
        'id': post.pk,
        'title': title,
        'excerpt': excerpt,
        'date': post_date,
        'time_ago': timesince(post_date, timezone.now()),
        'slug': post.post_name,
        'category': category,
        'category_slug': CATEGORY_SLUGS.get(category, 'default'),
        'category_color': CATEGORY_COLORS.get(category, '#e63946'),
        'image_url': get_post_image_url(post),
    }


def posts_by_category(posts, category, limit=2):
    return [p for p in posts if p['category'] == category][:limit]
