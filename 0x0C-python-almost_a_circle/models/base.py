#!/usr/bin/python3
"""Module base
Defines a Base class for other classes in the project
"""


class Base:
    """Base class
    Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a Base instance
        Args:
        - id: id of the instance
        """

        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nb_objects
