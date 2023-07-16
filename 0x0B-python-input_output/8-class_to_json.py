#!/usr/bin/python3
"""
class to json
"""
import json


def class_to_json(obj):
    """
    class to json
    convers a class to a json
    """
    attributes = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[attr] = value
    return str(attributes)
