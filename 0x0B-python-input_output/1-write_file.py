#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written
    """
    with open(filename, mode="w+") as file:
        return file.write(text)
