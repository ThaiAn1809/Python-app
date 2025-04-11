import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_user(email, name, password):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user(email, name, password) VALUES (?, ?, ?)', (email, name, password))
    conn.commit()
    conn.close()
    
def find_user_by_email(email):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password FROM user WHERE email = ?', (email, ))
    user = cursor.fetchone()
    conn.close()
    return user

def find_user_by_email_and_password(email, password):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password FROM user WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def find_user_by_id(user_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password, avatar FROM user WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_avatar(user_id, avatar):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('UPDATE user SET avatar = ? WHERE id = ?', (avatar,user_id))
    conn.commit()
    conn.close()
