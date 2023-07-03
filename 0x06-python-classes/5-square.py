#!/usr/bin/python3
class Square:
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

    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print('#', end='')
                print('')
