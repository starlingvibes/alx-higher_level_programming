#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    """
    with open(filename) as file:
        print(file.read(), end="")
