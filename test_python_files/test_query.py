"""asserts if data exists, if a database was created
and if the CRUD operations returned a result"""

from python_files.query import create, read, update, delete, query_1, query_2

payload = (2025, 15.00, 18.00, 20.00, 30.00, 50.00)


def test_create():
    table_name = "wages"
    data = "my_database.db"
    result = create(payload, data, table_name)
    assert result == "Record inserted successfully"


def test_read():
    result = read("my_database.db", "wages")
    assert isinstance(result, list)
    assert len(result) > 0


def test_update():
    year = 2021
    column = "year"
    new_value = 2023

    result = update("my_database.db", "wages", column, new_value, year)
    assert result == "Record updated successfully!"


def test_delete():
    year = 2012
    result = delete("my_database.db", "wages", year)
    assert result == "Record deleted successfully!"


def test_query_1():
    result_1 = query_1()
    assert result_1 is not None


def test_query_2():
    result_2 = query_2()
    assert result_2 is not None


if __name__ == "__main__":
    test_create()
    test_read()
    test_update()
    test_delete()
    test_query_1()
    test_query_2()

