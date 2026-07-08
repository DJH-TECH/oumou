import json
from pathlib import Path

import pymysql

OUTPUT_DIR = Path("data/afrikapulse221")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    db="afrikapulse221",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema=%s ORDER BY TABLE_NAME", ("afrikapulse221",))
        tables = [row["TABLE_NAME"] for row in cursor.fetchall()]

        for table in tables:
            print(f"Exporting {table}...")
            cursor.execute(f"SELECT * FROM `{table}`")
            rows = cursor.fetchall()
            output_file = OUTPUT_DIR / f"{table}.json"
            with output_file.open("w", encoding="utf-8") as f:
                json.dump(rows, f, ensure_ascii=False, indent=2, default=str)
            print(f"  Wrote {len(rows)} rows to {output_file}")
finally:
    connection.close()

print(f"Export complete. Files written to {OUTPUT_DIR.resolve()}")
