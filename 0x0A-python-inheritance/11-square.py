#!/usr/bin/python3
"""
Geometry module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class inheriting from the Rectangle class which inherits
    from the BaseGeometry class
    Private instance attributes:
        - width
        - height
    """
    def __init__(self, size):
        """
        Class constructor with private attributes
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method to calculate area
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns printable representation of the square instance
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
