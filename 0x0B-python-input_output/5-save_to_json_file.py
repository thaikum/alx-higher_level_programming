#!/usr/bin/python3

"""
json saver
"""
import json


def save_to_json_file(my_obj, filename):
    """
    json writer
    """
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(my_obj, file, ensure_ascii=False)
    except IOError:
        pass
