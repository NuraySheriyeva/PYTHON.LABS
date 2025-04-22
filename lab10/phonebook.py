import psycopg2
import pandas as pd
from config import load_config

def create_tables():
    """Create Tables in the Database"""
    commands = ["""CREATE TABLE IF NOT EXISTS phonebook (
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

    sql="""INSERT INTO phonebook(name, number) VALUES(%s, %s);"""

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

    sql="""INSERT INTO phonebook (name, number) VALUES(%s, %s);"""

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

    sql ="""UPDATE phonebook SET name=%s WHERE id=%s"""

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

    sql ="""UPDATE phonebook SET number=%s WHERE id=%s"""

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
    sql="""SELECT * FROM phonebook ORDER BY id;"""

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
    sql="""SELECT * FROM phonebook WHERE name ILIKE %s ORDER BY id;"""

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
    sql="""SELECT * FROM phonebook WHERE number LIKE %s ORDER BY id;"""

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
    sql = """DELETE FROM phonebook WHERE name=%s;"""
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

if __name__=='__main__':
    #create_tables()
    #console_input()
    #csv_phone("file.csv")
    #update_phone(3, "+77001001012")
    #everything()
    #filter_name("Nur")
    #filter_number("+7700100101")
    #delete_user("Nurkeldi")
    everything()