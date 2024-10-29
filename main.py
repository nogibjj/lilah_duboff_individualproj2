# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""
from python_files.extract import extract_data
from python_files.transform import transform
from python_files.query import create, read, update, delete, query_1, query_2

# import time

database = "my_database.db"
table = "wages"
url = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/wages_by_education%20copy.csv"
path = "data/wages_by_education_copy.csv"
folder = "data"
payload = (2025, 15.00, 18.00, 20.00, 30.00, 50.00)


# Extract
print("Extracting data...")
extract_data(url, path, folder)

# Transform and load/create
print("Transforming data...")
transform(path)

# CREATE
create(payload, database, table)

# READ
read(database, table)

# UPDATE
update(database, table, "year", 2026, 2022)

# DELETE
delete(database, table, 2021)

# Query
print("First query...")
print(query_1())
print("Second query...")
print(query_2())
