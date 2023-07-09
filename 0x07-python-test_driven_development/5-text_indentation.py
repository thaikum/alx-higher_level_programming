#!/usr/bin/python3

"""
This module prints a new line whenever it encounters .?:
"""


def text_indentation(text):
    """
    this function prints line with new line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    endLine = False
    for letter in text:
        if endLine:
            endLine = False
            print("\n")
            continue

        if letter in ".?:":
            endLine = True

        print(letter, end='')
