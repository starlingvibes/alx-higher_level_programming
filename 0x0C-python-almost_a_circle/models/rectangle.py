#!/usr/bin/python3
"""
Rectangle class inheriting from the Base class
"""


from models.base import Base


class Rectangle(Base):
    """
    Class describing a Rectangle
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance
        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @property
    def x(self):
        """retrieves the x attribute"""
        return selx.__x

    @property
    def y(self):
        """retrieves the y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
