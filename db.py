from contextlib import closing
import sqlite3

DB_NAME = 'popas.db'
SCHEMA = 'db_schema.sql'
SUPPORTED_ENTITIES = ['products', 'carts', 'users', 'items', 'cart_items', 'product_items']

def connect():
    return sqlite3.connect(DB_NAME)

def init():
    sql_file = open(SCHEMA)
    sql_as_string = sql_file.read()
    print(sql_as_string)
    with closing(connect()) as db_con, closing(db_con.cursor()) as cursor:
        cursor.executescript(sql_as_string)
        db_con.commit()

def row_to_dict(description, row):
    if row is None: return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d

def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result

def get(table):
    if table not in SUPPORTED_ENTITIES:
        return (False, [])
    with closing(connect()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT * FROM " + str(table))
        return (True, rows_to_dict(cur.description, cur.fetchall()))