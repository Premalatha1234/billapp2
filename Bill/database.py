import sqlite3
from datetime import datetime

DB_NAME = 'bill.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bills (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item TEXT,
                    quantity INTEGER,
                    price REAL,
                    amount REAL,
                    created_at TEXT
                )''')
    conn.commit()
    conn.close()

def insert_bill_item(item, quantity, price, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO bills (item, quantity, price, amount, created_at) VALUES (?, ?, ?, ?, ?)",
              (item, quantity, price, amount, timestamp))
    conn.commit()
    conn.close()
