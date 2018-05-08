import os

import psycopg2

def hello():
    return 'hello'

def hello_pg():
    conn = psycopg2.connect("host={0} dbname={1} user={2}".format(
        os.environ.get('PGHOST', '127.0.0.1'),
        os.environ.get('POSTGRES_DB', 'postgres'),
        os.environ.get('POSTGRES_USER', 'postgres')))

    cur = conn.cursor()
    cur.execute("select version()")
    version = cur.fetchone()[0]

    return version
