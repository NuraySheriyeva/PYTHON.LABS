import psycopg2
from config import load_config


def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    vendor_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (vendor_name,))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("ROW ADDED!")
        print(vendor_id)
        return vendor_id

def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                for vendor in vendor_list:
                    cur.execute(sql, vendor)
                    returned_id=cur.fetchone()
                    
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("Added many rows")



if __name__ == '__main__':
    insert_vendor("lol")    