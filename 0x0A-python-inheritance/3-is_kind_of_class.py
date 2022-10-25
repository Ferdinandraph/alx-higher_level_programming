#!/usr/bin/python3
"""function that returns True if the object is exactly an instance"""


def is_kind_of_class(obj, a_class):
    """method used in checking if an obj is in class

    Args:
        obj: an instance the class
        a_class: the class"""
    return isinstance(obj, a_class)
