#!/usr/bin/python3
"""
json file loader
"""
import json


def load_from_json_file(filename):
    """
    loads json file
    """
    with open(filename) as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
