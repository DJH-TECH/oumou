import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import connection

from siteweb.utils import fix_corrupted_text


WP_POSTS_COLUMNS = [
    'ID', 'post_author', 'post_date', 'post_date_gmt', 'post_content', 'post_title',
    'post_excerpt', 'post_status', 'comment_status', 'ping_status', 'post_password',
    'post_name', 'to_ping', 'pinged', 'post_modified', 'post_modified_gmt',
    'post_content_filtered', 'post_parent', 'guid', 'menu_order', 'post_type',
    'post_mime_type', 'comment_count',
]

TEXT_COLUMNS = {'post_content', 'post_title', 'post_excerpt', 'post_content_filtered'}

CREATE_TABLE_SQL = {
    'sqlite': """
        CREATE TABLE IF NOT EXISTS wp_posts (
            ID INTEGER PRIMARY KEY,
            post_author INTEGER NOT NULL DEFAULT 0,
            post_date TEXT NOT NULL,
            post_date_gmt TEXT NOT NULL,
            post_content TEXT NOT NULL,
            post_title TEXT NOT NULL,
            post_excerpt TEXT NOT NULL,
            post_status TEXT NOT NULL DEFAULT 'publish',
            comment_status TEXT NOT NULL DEFAULT 'open',
            ping_status TEXT NOT NULL DEFAULT 'open',
            post_password TEXT NOT NULL DEFAULT '',
            post_name TEXT NOT NULL DEFAULT '',
            to_ping TEXT NOT NULL,
            pinged TEXT NOT NULL,
            post_modified TEXT NOT NULL,
            post_modified_gmt TEXT NOT NULL,
            post_content_filtered TEXT NOT NULL,
            post_parent INTEGER NOT NULL DEFAULT 0,
            guid TEXT NOT NULL DEFAULT '',
            menu_order INTEGER NOT NULL DEFAULT 0,
            post_type TEXT NOT NULL DEFAULT 'post',
            post_mime_type TEXT NOT NULL DEFAULT '',
            comment_count INTEGER NOT NULL DEFAULT 0
        )
    """,
    'mysql': """
        CREATE TABLE IF NOT EXISTS wp_posts (
            ID BIGINT AUTO_INCREMENT PRIMARY KEY,
            post_author BIGINT UNSIGNED NOT NULL DEFAULT 0,
            post_date DATETIME NOT NULL,
            post_date_gmt DATETIME NOT NULL,
            post_content LONGTEXT NOT NULL,
            post_title TEXT NOT NULL,
            post_excerpt TEXT NOT NULL,
            post_status VARCHAR(20) NOT NULL DEFAULT 'publish',
            comment_status VARCHAR(20) NOT NULL DEFAULT 'open',
            ping_status VARCHAR(20) NOT NULL DEFAULT 'open',
            post_password VARCHAR(255) NOT NULL DEFAULT '',
            post_name VARCHAR(200) NOT NULL DEFAULT '',
            to_ping TEXT NOT NULL,
            pinged TEXT NOT NULL,
            post_modified DATETIME NOT NULL,
            post_modified_gmt DATETIME NOT NULL,
            post_content_filtered LONGTEXT NOT NULL,
            post_parent BIGINT UNSIGNED NOT NULL DEFAULT 0,
            guid VARCHAR(255) NOT NULL DEFAULT '',
            menu_order INT NOT NULL DEFAULT 0,
            post_type VARCHAR(20) NOT NULL DEFAULT 'post',
            post_mime_type VARCHAR(100) NOT NULL DEFAULT '',
            comment_count BIGINT NOT NULL DEFAULT 0
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """,
}


class Command(BaseCommand):
    help = 'Importe les articles WordPress depuis data/afrikapulse221/wp_posts.json'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Vide la table wp_posts avant import',
        )

    def handle(self, *args, **options):
        data_file = Path('data/afrikapulse221/wp_posts.json')
        if not data_file.exists():
            self.stderr.write(self.style.ERROR(f'Fichier introuvable : {data_file}'))
            return

        vendor = connection.vendor
        create_sql = CREATE_TABLE_SQL.get(vendor)
        if not create_sql:
            self.stderr.write(self.style.ERROR(f'Base de données non supportée : {vendor}'))
            return

        with connection.cursor() as cursor:
            cursor.execute(create_sql)
            if options['clear']:
                cursor.execute('DELETE FROM wp_posts')

            cursor.execute('SELECT COUNT(*) FROM wp_posts')
            existing = cursor.fetchone()[0]
            if existing and not options['clear']:
                self.stdout.write(
                    self.style.WARNING(
                        f'{existing} articles déjà présents. Utilisez --clear pour réimporter.'
                    )
                )
                return

            with data_file.open(encoding='utf-8') as f:
                rows = json.load(f)

            placeholders = ', '.join(['%s'] * len(WP_POSTS_COLUMNS))
            columns = ', '.join(f'`{col}`' if vendor == 'mysql' else col for col in WP_POSTS_COLUMNS)
            insert_sql = f'INSERT INTO wp_posts ({columns}) VALUES ({placeholders})'

            batch = []
            for row in rows:
                values = []
                for col in WP_POSTS_COLUMNS:
                    value = row.get(col, '')
                    if col in TEXT_COLUMNS and isinstance(value, str):
                        value = fix_corrupted_text(value)
                    values.append(value)
                batch.append(tuple(values))
                if len(batch) >= 500:
                    cursor.executemany(insert_sql, batch)
                    batch.clear()

            if batch:
                cursor.executemany(insert_sql, batch)

        self.stdout.write(self.style.SUCCESS(f'{len(rows)} articles importés dans wp_posts.'))
