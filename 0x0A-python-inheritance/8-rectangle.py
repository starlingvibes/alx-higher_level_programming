#!/usr/bin/python3
"""
Geometry module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class inheriting from the BaseGeometry class
    Private instance attributes:
        -width
        -height
    """
    def __init__(self, width, height):
        """
        Class constructor with private attributes
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
