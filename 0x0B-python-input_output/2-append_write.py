#!/usr/bin/python3

"""
file writer
"""


def append_write(filename="", text=""):
    """
    writer function
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
