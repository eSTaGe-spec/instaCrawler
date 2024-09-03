import sqlite3


def create_connection(db):
    conn = sqlite3.connect(db)
    return conn


def create_table(conn):
    table_create = '''
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        bio TEXT,
        name TEXT,
        media INTEGER,
        followers INTEGER,
        followees INTEGER,
        avatar_url TEXT
    );
    '''

    cursor = conn.cursor()
    cursor.execute(table_create)
    conn.commit()


def save_data_profile(conn, data):
    save_data = '''
    INSERT OR REPLACE INTO profiles (username, bio, name, media, followers, followees, avatar_url) 
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    cursor = conn.cursor()
    cursor.execute(save_data, (
        data['username'],
        data['bio'],
        data['name'],
        data['media'],
        data['followers'],
        data['followees'],
        data['avatar_url']
    ))

    conn.commit()
