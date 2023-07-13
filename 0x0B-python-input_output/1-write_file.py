#!/usr/bin/python3

"""
file writer
"""


def write_file(filename="", text=""):
    """
    writer function
    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
