"""This file takes the csv data and converts it into a database/.db file"""

from python_files.transform import transform


def test_transform():
    transform_result = transform("data/wages_by_education_copy.csv")
    assert transform_result is not None


if __name__ == "__main__":
    test_transform()
