#!/usr/bin/python3
"""raises an exception"""


class BaseGeometry:
    """class to be implemented"""

    def area(self):
        """instance method that raises an exception"""

        raise Exception("area() is not implemented")
