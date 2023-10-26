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
        if type(size) is int or type(size) is float:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be a number")

    def area(self):
        """ Area of the square

        this is a public instance method that compute the area of the Square

        Args:
            No Args.

        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value

    def __eq__(self, other):
        """ compares two object for equality """
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equal to """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Greater Than """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Greater than or Equal to """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Less than """
        return self.area() < other.area()

    def __le__(self, other):
        """ Less than or equal to """
        return self.area() <= other.area()
