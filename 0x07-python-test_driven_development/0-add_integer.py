#!/usr/bin/python3
"""
This module contains one function add_integer that adds
two integers or float
"""


def add_integer(a, b=98):
    """
    this function ads two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
