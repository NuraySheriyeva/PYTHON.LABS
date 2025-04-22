import psycopg2
import pandas as pd
from config import load_config

def create_tables():
    """Create Tables in the Database"""
    commands = ["""CREATE TABLE IF NOT EXISTS phonebook_11 (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL, 
                number VARCHAR(20) NOT NULL)"""]
    
    try:
        config=load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        print("Table created")
    
def insert_phone(name, number):
    """Insert new caller into the table"""

    sql="""INSERT INTO phonebook_11(name, number) VALUES(%s, %s);"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, number))
                print("User added")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
def console_input():
    name=input("Enter name: ")
    number=input("Enter phone number: ")
    insert_phone(name, number)

def csv_phone(file):
    df = pd.read_csv(file)
    config=load_config()

    sql="""INSERT INTO phonebook_11 (name, number) VALUES(%s, %s);"""

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for index, row in df.iterrows():
                    cur.execute(sql, (row['name'], row['number']))
                print("User added via CSV")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def update_name(id, name):
    """Update name"""

    update_row_count=0

    sql ="""UPDATE phonebook_11 SET name=%s WHERE id=%s"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, id))
                update_row_count= cur.rowcount
                print("Updated")
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return update_row_count

def update_phone(id, number):
    """Update number"""

    update_row_count=0

    sql ="""UPDATE phonebook_11 SET number=%s WHERE id=%s"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (number, id))
                update_row_count= cur.rowcount
                print("Updated")
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return update_row_count

def everything():
    sql="""SELECT * FROM phonebook_11 ORDER BY id;"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows=cur.fetchall()
                for row in rows:
                    print(row)
                print("Everything is printed")
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def filter_name(name):
    sql="""SELECT * FROM phonebook_11 WHERE name ILIKE %s ORDER BY id;"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name+'%',))
                rows=cur.fetchall()
                for row in rows:
                    print(row)
                print(f"Every '{name}' is printed")
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def filter_number(number):
    sql="""SELECT * FROM phonebook_11 WHERE number LIKE %s ORDER BY id;"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (number+'%',))
                rows=cur.fetchall()
                for row in rows:
                    print(row)
                print(f"Every '{number}' is printed")
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def delete_user(name):
    '''DELETE phone by name'''

    rows_deleted=0
    sql = """DELETE FROM phonebook_11 WHERE name=%s;"""
    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, ))
                rows_deleted=cur.rowcount

                print(f"Shall '{name}' be demolished!")

            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return rows_deleted

def surname_column():
    sql="""ALTER TABLE phonebook_11 ADD COLUMN surname VARCHAR(100);"""

    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                print("Column 'surname' added")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def pattern_filter(column, pattern):
    if column not in ['name', 'surname', 'number', 'id']:
        print("Enter valid column")
        return
    
    sql="""SELECT * FROM pattern_filter_sql(%s, %s);"""
    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (column, pattern+'%'))
                rows=cur.fetchall()
                for row in rows:
                    print(row)
                print(f"Rows with {pattern} in the {column}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def call_insert_or_update(name, phone, surname):
    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""CALL insert_or_update_user(%s, %s, %s);""", (name,phone, surname))
                print("Procedure done")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_many(names, phones):
    config = load_config()
    invalid_entries = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""CALL insert_many_users(%s, %s)""", (names, phones,))
            print("UserS added")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
    return invalid_entries

def users_page(limit, offset):
    config = load_config()
    users = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_users_page(%s, %s);", (limit, offset))
                users = cur.fetchall()
                for user in users:
                    print(user)
            print(f"Users from {offset} to {limit} are printed")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
    return users

def delete_by_nameORphone(name, phone):
    config=load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""CALL delete_user(%s, %s);""", (name, phone, ))
            print("User deleted")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__=='__main__':
    create_tables()
    #console_input()
    #csv_phone("file.csv")
    #update_phone(7, "+77001001016")
    #update_name(6, "Aliguriyakerim")
    #everything()
    #filter_name("Nur")
    #filter_number("+7700100101")
    #delete_user("Nurkeldi")
    #everything()
    #pattern_filter("name", "Ali")
    #insert_user("Top 5", "+77001001018", "Machine")
    #call_insert_or_update("Alina", "+77001001025", "Chinova")
    names=['KBTU', 'Karaganda Auto']
    phones=['+77011111111', '+77011001022']
    #insert_many(names, phones)
    #users_page(5, 0)
    #delete_by_nameORphone("Keruen", "NULL")
