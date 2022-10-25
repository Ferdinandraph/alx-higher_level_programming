#!/usr/bin/python3
"""function that returns true if the object is an\
    instance of the inherited class"""


def inherits_from(obj, a_class):
    """the function used to implement

    Args:
        obj: the object
        a_class: the class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
