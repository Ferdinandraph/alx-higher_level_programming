#!/usr/bin/python3
"""a BaseGeometry"""


class BaseGeometry:
    """class to be implemented"""

    def area(self):
        """instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """an instance method that validates value

        Args:
            name: name of value
            value: the value"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
