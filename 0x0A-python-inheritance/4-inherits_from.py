#!/usr/bin/python3
"""
issubclass module
"""


def inherits_from(obj, a_class):
    """
    if it inherits return true
    """
    return issubclass(obj.__class__, a_class) and type(obj) != a_class
