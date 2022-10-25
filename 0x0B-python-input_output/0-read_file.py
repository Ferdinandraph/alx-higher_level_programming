#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """the function to be implemented"""

    with open(filename, encoding= "utf-8") as fname:
        print(fname.read(), end='')
