import sqlite3
from pathlib import Path

#DBMS - СУБД

def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent / 'db.sqlite3')
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    productsID INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    image TEXT
    )
    """)


if __name__ == '__main__':
    init_db()