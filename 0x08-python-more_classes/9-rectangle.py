#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """represent a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int, optional): _width of the Rectanle_. Defaults to 0.
            height (int, optional): _height of the Rectangle_. Defaults to 0.
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """Returns the area of a triangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a triangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the biggest area

        Args:
            rect_1(Rectangle): The first rectangle
            rect_2(Rectangle): The second rectangle
            """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance

        Args:
            size (int): This is equal to the width and height of the triangle
        """
        return (cls(size, size))

    def __str__(self):
        """Represent the Rectangle with the character #

        Returns:
            the printable representation of the triangle
        """
        if self.__width == 0 or self.__height == 0:
            print('')
        rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                (rec.append("#"))
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """for every deletion of a rectangle instance, a message is printed"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
