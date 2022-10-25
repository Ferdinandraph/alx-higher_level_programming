#!/usr/bin/python3
"""defines the function read_file"""


def read_file(filename=""):
    """function that reads a text file in UTF-8"""

    with open(filename, encoding="utf-8") as fname:
        print(fname.read(), end='')
