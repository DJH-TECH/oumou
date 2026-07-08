import json
import re
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlparse

from django.templatetags.static import static

DATA_DIR = Path('data/afrikapulse221')
LOCAL_IMAGE_DIR = Path('siteweb/static/siteweb/images/articles')
WP_MEDIA_BASE = 'https://afrikapulse221.com'


def normalize_image_url(url):
    if not url:
        return None
    url = url.strip().replace('\\/', '/')
    if url.startswith('//'):
        url = 'https:' + url
    if 'wp-content/uploads' in url:
        match = re.search(r'/wp-content/uploads/.+', url)
        if match:
            path = match.group(0).split('?')[0].split('#')[0]
            return WP_MEDIA_BASE + path
    if url.startswith('/wp-content/'):
        return WP_MEDIA_BASE + url.split('?')[0].split('#')[0]
    return url


def extract_image_url(content):
    if not content:
        return None
    patterns = [
        r'<img[^>]+src=["\']([^"\']+)["\']',
        r'background-image:\s*url\(["\']?([^"\')\s]+)["\']?\)',
        r'srcset=["\']([^"\']+)["\']',
    ]
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if not match:
            continue
        candidate = match.group(1).strip()
        if pattern.endswith('srcset=["\']([^"\']+)["\']'):
            candidate = candidate.split(',')[0].strip().split()[0]
        return normalize_image_url(candidate)
    return None


@lru_cache(maxsize=1)
def _image_maps():
    thumbnails = {}
    attached_files = {}
    yoast_images = {}

    postmeta_file = DATA_DIR / 'wp_postmeta.json'
    if postmeta_file.exists():
        with postmeta_file.open(encoding='utf-8') as f:
            for row in json.load(f):
                post_id = row.get('post_id')
                key = row.get('meta_key')
                value = row.get('meta_value')
                if key == '_thumbnail_id' and str(value).isdigit():
                    thumbnails[post_id] = int(value)
                elif key == '_wp_attached_file' and value:
                    attached_files[post_id] = value

    yoast_file = DATA_DIR / 'wp_yoast_indexable.json'
    if yoast_file.exists():
        with yoast_file.open(encoding='utf-8') as f:
            for row in json.load(f):
                if row.get('object_type') != 'post':
                    continue
                if row.get('object_sub_type') not in (None, 'post'):
                    continue
                image = row.get('open_graph_image')
                if image:
                    yoast_images[row['object_id']] = image

    return thumbnails, attached_files, yoast_images


def _url_from_attachment(attachment_id, attached_files):
    rel_path = attached_files.get(attachment_id)
    if not rel_path:
        return None
    return f'{WP_MEDIA_BASE}/wp-content/uploads/{rel_path.lstrip("/")}'


def _local_image_path(post_id):
    if not LOCAL_IMAGE_DIR.exists():
        return None
    for ext in ('.jpg', '.jpeg', '.png', '.webp', '.gif'):
        candidate = LOCAL_IMAGE_DIR / f'{post_id}{ext}'
        if candidate.exists():
            return static(f'siteweb/images/articles/{post_id}{ext}')
    return None


def resolve_post_image_url(post):
    """Résout l'image d'un article via contenu, miniature WP ou Yoast SEO."""
    post_id = post.pk
    thumbnails, attached_files, yoast_images = _image_maps()

    for candidate in (
        extract_image_url(post.post_content),
        _url_from_attachment(thumbnails.get(post_id), attached_files),
        normalize_image_url(yoast_images.get(post_id)),
    ):
        if candidate:
            return candidate
    return None


def get_post_image_url(post, prefer_local=True):
    if prefer_local:
        local = _local_image_path(post.pk)
        if local:
            return local
    return resolve_post_image_url(post)


def local_image_filename(post_id, url):
    path = urlparse(url).path
    ext = Path(path).suffix.lower()
    if ext not in {'.jpg', '.jpeg', '.png', '.webp', '.gif'}:
        ext = '.jpg'
    return f'{post_id}{ext}'
