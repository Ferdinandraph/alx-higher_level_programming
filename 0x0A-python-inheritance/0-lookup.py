#!/usr/bin/python3
"""function that returns the list of available attribute and methods"""


def lookup(obj):
    """the lookup function


    Args:
        obj: contains all methods and attributes"""
    return dir(obj)
