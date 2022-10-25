#!/usr/bin/python3
"""defines write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file

    Args:
        filename: name of the text file
        text: the text to be written to the text file
        """

    with open(filename, "w", encoding="utf-8") as fname:
        return fname.write(text)
