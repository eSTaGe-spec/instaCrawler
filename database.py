import sqlite3


def create_connection(db):
    """
    Функция для подключения к базе данных
    """

    conn = sqlite3.connect(db)
    return conn


def create_table(conn):
    """
    Функция для создания таблицы profiles в базе данных
    """

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
    """
    Функция для сохранения данных пользователя в базу данных
    """

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
