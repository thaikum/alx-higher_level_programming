#!/usr/bin/python3

"""
custom int
"""


class MyInt(int):
    """
    for inversion
    """

    def __eq__(self, num):
        return int(self) != num
