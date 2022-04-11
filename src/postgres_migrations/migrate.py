import os
from os import walk
import psycopg


USER = os.environ.get("POSTGRES_DB_USER")
PASSWORD = os.environ.get("POSTGRES_DB_PASSWORD")
HOST = os.environ.get("POSTGRES_DB_HOST")
DBNAME = os.environ.get("POSTGRES_DB_NAME")


if __name__ == '__main__':

    conn = psycopg.connect(
        host=HOST,
        dbname=DBNAME,
        user=USER,
        password=PASSWORD)
    conn.autocommit = True

    f = []
    for (dirpath, dirnames, filenames) in walk("./scripts"):
        f.extend(filenames)
        break

    dirname = os.path.dirname(__file__)

    scripts = []
    for file in f:
        scripts.append(os.path.join(dirname, "scripts", file))

    cursor = conn.cursor()
    print("hello!")
    for script in scripts:
        with open(script) as f:
            for line in f:
                sql = line.strip()
                print(sql)

                try:
                    cursor.execute(sql)
                except psycopg.errors.DuplicateObject as err:
                    print(err)

    conn.close()
