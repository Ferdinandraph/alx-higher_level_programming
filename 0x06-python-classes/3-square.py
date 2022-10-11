#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """init initializes the size attribute to the class

        Args:
        size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
