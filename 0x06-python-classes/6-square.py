#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (isinstance(position, tuple)
                and len(position) == 2
                and isinstance(position[0], int)
                and isinstance(position[1], int)):
            self.__position = position

        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for x in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')

                for y in range(self.__size):
                    print('#', end='')
                print('')
