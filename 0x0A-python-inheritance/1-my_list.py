#!/usr/bin/python3
"""
Class my_list
"""


class MyList(list):
    """
    inheriting list
    """

    def print_sorted(self):
        print(sorted(self))
