#!/usr/bin/python3
"""defines an append_write function"""


def append_write(filename="", text=""):
    """function that appends a string at the\
        end of a text file

    Args:
        filename: the name of the text file
        text: the text to append
        """

    with open(filename, "a", encoding="utf-8") as fname:
        return fname.write(text)
