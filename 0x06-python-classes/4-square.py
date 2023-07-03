#!/usr/bin/python3
"""
Square class
"""


class Square:
    """
    initialization area calculation and use of getters
    and setters
    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
