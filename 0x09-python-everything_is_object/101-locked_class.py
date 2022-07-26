#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevents the user from creating new instance attributes for
    anything but 'first_name'
    """

    __slots__ = ["first_name"]
