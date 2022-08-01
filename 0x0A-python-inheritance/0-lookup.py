#!/usr/bin/python3
"""
Finding a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of attributes and methods for an object
    """
    return dir(obj)
