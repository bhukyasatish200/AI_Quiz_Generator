"""
Test Database
"""

import sqlite3

from config.settings import DATABASE_PATH

def test_database():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = cursor.fetchall()

    print("=" * 60)
    print("DATABASE TABLES")
    print("=" * 60)

    for table in tables:
        print(table[0])

    print("=" * 60)
    print("Total Tables :", len(tables))
    print("=" * 60)

    conn.close()


if __name__ == "__main__":
    test_database()