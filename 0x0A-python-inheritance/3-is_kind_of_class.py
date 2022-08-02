#!/usr/bin/python3
"""
Check same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from the specified class

    Otherwise, returns False
    """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    return False
