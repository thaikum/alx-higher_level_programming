#!/usr/bin/python3
"""
This module contains a function square that
prints a square of #
"""


def print_square(size):
    """
    This function prints a square using #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end='')
        print("")
