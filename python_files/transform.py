# This file should take the cvs data and convert it into a database, or .db file
# performs the CREATE from CRUD operations
import sqlite3
import csv


def transform(data):
    """Transforms and loads data into the database"""

    payload = csv.reader(open(data, newline=""), delimiter=",")
    next(payload)

    conn = sqlite3.connect("./sqlite/my_database.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS wages")
    c.execute(
        """
              CREATE TABLE wages (
                    year INTEGER,
                    less_than_hs REAL,
                    high_school REAL,
                    some_college REAL,
                    bachelors_degree REAL,
                    advanced_degree REAL
                  )
              """
    )
    # insert
    c.executemany("""INSERT INTO wages VALUES (?, ?, ?, ?, ?, ?)""", payload)
    conn.commit()
    conn.close()
    print(payload)
    return payload
