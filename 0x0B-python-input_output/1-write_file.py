#!/usr/python3

"""
file writer
"""


def write_file(filename="", text=""):
    """
    writer function
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)