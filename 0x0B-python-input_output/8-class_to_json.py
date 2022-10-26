#!/usr/bin/python3
"""defines class to json"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    des = {}

    if hasattr(obj, __dict__):
        des = obj.__dict__.copy()
        return des
