# db/setup_db.py

import sqlite3

def init_db(db_path="db/invoices.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            invoice_amount REAL,
            product_name TEXT
        )
    """)
    conn.commit()
    conn.close()
