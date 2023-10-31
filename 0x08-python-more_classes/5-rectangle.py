#!/usr/bin/python3
"""
==================
module 5-rectangle
==================
"""


class Rectangle:
    """insantiate the attributes"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrive property"""

        return self.__width

    @width.setter
    def width(self, value):
        """return width as an int"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive property"""

        return self.__height

    @height.setter
    def height(self, value):
        """return height as an int"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle shape with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for i in range(self.__height):
            rows = ""
            for j in range(self.__width):
                rows += "#"
            result.append(rows)
        output = "\n".join(result)
        return output

    def __repr__(self):
        """return rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """return a message after deletion"""

        print("Bye rectangle...")
