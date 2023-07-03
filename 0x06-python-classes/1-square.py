#!/usr/bin/python3
"""
 This module creates a square and initializes it with 
 an integer value
"""
class Square:
    """
    the constructor initializes size
    as an instance variable
    """
    
    def __init__(self, size: int):
        self.__size = size
