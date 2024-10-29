import sqlite3


def create(payload, data, table):
    """Create and insert into table"""
    conn = sqlite3.connect(data)
    c = conn.cursor()
    c.execute(
        f"""
              CREATE TABLE IF NOT EXISTS {table} (
                    year INTEGER,
                    less_than_hs REAL,
                    high_school REAL,
                    some_college REAL,
                    bachelors_degree REAL,
                    advanced_degree REAL
                  )
              """
    )

    query = f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?)"
    c.execute(query, payload)

    conn.commit()
    conn.close()

    print("Record inserted successfully")
    return "Record inserted successfully"


def read(data, table):
    """Read data from the table"""
    conn = sqlite3.connect(data)
    c = conn.cursor()

    query = f"SELECT * FROM {table} LIMIT 10"
    c.execute(query)

    read_result = c.fetchall()
    conn.close()

    return read_result


def update(data, table, column, new_value, year):
    """Update a specific column in a row based on year"""
    conn = sqlite3.connect(data)
    c = conn.cursor()
    query = f"UPDATE {table} SET {column} = ? WHERE year = ?"
    c.execute(query, (new_value, year))
    affected_rows = c.rowcount
    conn.commit()
    c.close()
    conn.close()

    if affected_rows == 0:
        print("No record found")
        return "No record found"
    print("Record updated successfully!")
    return "Record updated successfully!"


def delete(database, table, year):
    """Delete a specific column in a row based on year"""
    conn = sqlite3.connect(database)
    c = conn.cursor()
    query = f"DELETE FROM {table} WHERE year = ?"
    c.execute(query, (year,))
    changed_rows = c.rowcount
    conn.commit()
    c.close()
    conn.close()

    if changed_rows == 0:
        print("No record found")
        return "No record found"
    print("Record deleted successfully!")
    return "Record deleted successfully!"


def query_1():
    """queries the db for top five rows"""
    conn = sqlite3.connect("my_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM wages LIMIT 5")
    print("Top 5 rows of the wages table:")
    query_1_result = c.fetchall()
    print("Query is complete")
    conn.close()
    return query_1_result


def query_2():
    """queries the db for average wage based on level of education"""
    conn = sqlite3.connect("my_database.db")
    c = conn.cursor()
    c.execute(
        "SELECT year, AVG(less_than_hs), AVG(high_school), AVG(some_college), AVG(bachelors_degree), AVG(advanced_degree) FROM wages WHERE year > 2010 GROUP BY year"
    )
    print("Average hourly pay from wages table, based on education level:")
    query_2_result = c.fetchall()
    print("Query is complete!")
    conn.close()
    return query_2_result
