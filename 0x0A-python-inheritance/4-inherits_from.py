#!/usr/bin/python3
"""
Checks if only a subclass of
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited from the specified class
    """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    return False
