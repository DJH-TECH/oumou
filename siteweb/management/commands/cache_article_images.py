import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from django.core.management.base import BaseCommand

from siteweb.models import WpPosts
from siteweb.wp_images import LOCAL_IMAGE_DIR, get_post_image_url, local_image_filename, resolve_post_image_url


class Command(BaseCommand):
    help = 'Télécharge les images des articles depuis afrikapulse221.com'

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, default=0, help='Nombre max d articles (0 = tous)')
        parser.add_argument('--force', action='store_true', help='Retélécharger même si déjà en cache')

    def handle(self, *args, **options):
        LOCAL_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
        posts = WpPosts.objects.filter(post_status='publish', post_type='post').order_by('-post_date')
        if options['limit']:
            posts = posts[:options['limit']]

        downloaded = 0
        skipped = 0
        failed = 0

        for post in posts:
            remote_url = resolve_post_image_url(post)
            if not remote_url:
                self.stdout.write(self.style.WARNING(f'Pas d image : {post.pk} - {post.post_title[:50]}'))
                failed += 1
                continue

            filename = local_image_filename(post.pk, remote_url)
            target = LOCAL_IMAGE_DIR / filename

            if target.exists() and not options['force']:
                skipped += 1
                continue

            try:
                request = Request(remote_url, headers={'User-Agent': 'AfrikaPulse221-Django/1.0'})
                with urlopen(request, timeout=20) as response:
                    data = response.read()
                if len(data) < 500:
                    raise ValueError('fichier trop petit')
                target.write_bytes(data)
                downloaded += 1
                self.stdout.write(self.style.SUCCESS(f'OK {post.pk} -> {filename}'))
                time.sleep(0.15)
            except (URLError, TimeoutError, ValueError) as err:
                failed += 1
                self.stdout.write(self.style.ERROR(f'Echec {post.pk} : {err}'))

        self.stdout.write(self.style.SUCCESS(
            f'Terminé : {downloaded} téléchargées, {skipped} déjà en cache, {failed} échecs.'
        ))
