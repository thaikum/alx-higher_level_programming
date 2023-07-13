#!/usr/bin/python3

"""
reading files
"""


def read_file(filename=""):
    """
    file reader
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
