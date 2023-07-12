#!/usr/bin/python3

"""
custom int
"""


class MyInt(int):
    """
    for inversion
    """

    def __eq__(self, num):
        return super().__ne__(num)

    def __ne__(self, num):
        return super().__eq__(num)
