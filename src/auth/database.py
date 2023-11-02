import sqlite3
from src.utils.paths import users_database


def add_user(username, password):
    conn = sqlite3.connect(users_database); cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit(); conn.close()

def get_all_users():
    conn = sqlite3.connect(users_database); cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
    

def only_oneTime():
    conn = sqlite3.connect(users_database); cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit(); conn.close()
    