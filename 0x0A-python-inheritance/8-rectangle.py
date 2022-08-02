#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class inheriting from the BaseGeometry class
    """
    def __init__(self, width, height):
        """ 
        Class constructor with private attributes
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
