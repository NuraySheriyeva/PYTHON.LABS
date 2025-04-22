import sys
import os
from configparser import ConfigParser
from snake_main import run_game
# Add the project root (work/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import psycopg2

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def create_tables(conn):
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL
        )
        """,
        """CREATE TABLE IF NOT EXISTS user_score(
            id INTEGER PRIMARY KEY REFERENCES users(id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL
        )""")
    try:
        config = load_config()
        with conn.cursor() as cur:
            # execute the CREATE TABLE statement
            for command in commands:
                cur.execute(command)
        print("Tables created")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
def get_or_create_user(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
            user_id = cur.fetchone()[0]
            conn.commit()
            return user_id

def insert_update(conn, user_id, score, level):
    config = load_config()

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM user_score WHERE id = %s", (user_id,))
            if cur.fetchone():
                cur.execute(""" UPDATE user_score SET score = %s, level = %s WHERE id = %s;""", (score, level, user_id))
                print("Updated score")
            else:
                cur.execute(""" INSERT INTO user_score (id, score, level) VALUES (%s, %s, %s) """, (user_id, score, level))
                print("User added, score saved")
        conn.commit()
    except Exception as error:
        print(error)



if __name__ == '__main__':

    username=input("Enter username: ").strip()
    

    try:
        config=load_config()
        conn=psycopg2.connect(**config)
        create_tables(conn)
        user_id = get_or_create_user(conn, username)
        def save_callback(user_id, game_score, level):
            insert_update(user_id, game_score, level)
        game_score, level = run_game(save_callback=save_callback, user_id=user_id)
        insert_update(conn, user_id, game_score, level)
        conn.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
