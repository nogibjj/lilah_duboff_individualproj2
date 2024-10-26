# can use this file to extract csv from a url
""" This file can take csv data from a url and extract it to be transformed and queried """

import requests
import os


def extract_data(url, path, directory):
    """Extract data from a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(path, "wb") as f:
            f.write(r.content)
    return path