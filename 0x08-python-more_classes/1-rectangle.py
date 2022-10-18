#!/usr/bin/python3
"""defines a Rectangle class"""


class Rectangle:
    """represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int, optional): _width of the Rectanle_. Defaults to 0.
            height (int, optional): _height of the Rectangle_. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter representation of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter representation of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the getter representation of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter representation of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
