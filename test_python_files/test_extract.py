"""Asserting that the Data is being extracted from the url"""

from python_files.extract import extract_data
import os


def test_extract_data():
    url = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/wages_by_education%20copy.csv"
    test_path = "data/wages_by_education_copy.csv"
    folder = "data"
    result = extract_data(url, test_path, folder)
    assert os.path.exists(result)



if __name__ == "__main__":
    test_extract_data()
