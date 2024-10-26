# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""

from SQL_files.extract import extract_data
from SQL_files.transform import transform
from SQL_files.query import create, read, update, delete, query_1, query_2
import time

database = "remotehealthDB.db"
table = "remote_health"
url = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/Impact_of_Remote_Work_on_Mental_Health.csv"
path = "data/remote_work_mental_health_data.csv"
folder = "data"
payload = (
    "EMP5001",
    37,
    "Non-binary",
    "Nurse",
    "Healthcare",
    12,
    "Hybrid",
    46,
    7,
    2,
    "Low",
    "Depression",
    "No",
    "Decrease",
    1,
    "Unsatisfied",
    1,
    "Weekly",
    "Good",
    "Europe",
)


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
update(database, table, "Age", 35, "EMP0040")

# DELETE
delete(database, table, "EMP0040")


# Query
print("First query...")
print(query_1())
print("Second query...")
print(query_2())