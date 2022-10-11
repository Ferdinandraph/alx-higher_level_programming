#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """init initializes the size attribute to the class

        Args:
        size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """get the current value of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the current value of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area of the square."""
        return (self.size * self.size)
