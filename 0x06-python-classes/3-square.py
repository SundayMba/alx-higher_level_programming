#!/usr/bin/python3

"""Square module: this class <Square> models a Square object"""


class Square:
    """ square class

    this class is a minimal square class with no implementation
    just pass.

    """
    def __init__(self, size=0):
        """ __init__ method

        this method is a special method that acts as an instance
        constructor after instantiation

        Args:
            size (int): <size> is a private attribute of type integer.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of the square

        this is a public instance method that compute the area of the Square

        Args:
            No Args.

        """
        return (self.__size ** 2)
