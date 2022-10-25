#!/usr/bin/python3
"""defines to_json_string function"""
import json


def to_json_string(my_obj):
    """function that returns the json rep of an obj(str)

    Args:
        my_obj: the object string"""

    return json.dumps(my_obj)
