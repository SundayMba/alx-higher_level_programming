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

    def my_print(self):
        """ instance method

        my_print - print the value of __size with the character #

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
