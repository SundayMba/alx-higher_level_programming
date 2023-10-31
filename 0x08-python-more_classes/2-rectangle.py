#!/usr/bin/python3
"""create a class"""


class Rectangle:
    """instantiate attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """check if width is an integer"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height"""

        return self.__height

    @height.setter
    def height(self, value):
        """check if height is an integer"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area"""

        return self.__width * self.__height

    def perimeter(self):
        """return perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
