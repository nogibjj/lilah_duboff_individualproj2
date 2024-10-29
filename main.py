# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""
import time
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
start_time = time.time()
extract_data(url, path, folder)
end_time = time.time()
print(f"Extraction took {end_time - start_time:.2f} seconds.\n")

# Transform and load/create
print("Transforming data...")
start_time = time.time()
transform(path)
end_time = time.time()
print(f"Transformation took {end_time - start_time:.2f} seconds.\n")


# CREATE
start_time = time.time()
create(payload, database, table)
end_time = time.time()
print(f"CREATE took {end_time - start_time:.2f} seconds.\n")

# READ
start_time = time.time()
read(database, table)
end_time = time.time()
print(f"READ took {end_time - start_time:.2f} seconds.\n")

# UPDATE
start_time = time.time()
update(database, table, "year", 2026, 2022)
end_time = time.time()
print(f"UPDATE took {end_time - start_time:.2f} seconds.\n")

# DELETE
start_time = time.time()
delete(database, table, 2021)
end_time = time.time()
print(f"DELETE took {end_time - start_time:.2f} seconds.\n")


# Query
start_time = time.time()
print("First query...")
print(query_1())
print("Second query...")
print(query_2())
end_time = time.time()
print(f"QUERIES took {end_time - start_time:.2f} seconds.\n")
