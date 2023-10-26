#!/usr/bin/python3

"""Square module: this class <Square> models a Square object"""


class Square:
    """ square class

    this class is a minimal square class with no implementation
    just pass.

    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method

        this method is a special method that acts as an instance
        constructor after instantiation

        Args:
            size (int): <size> is a private attribute of type integer.
            position (tuple): a tuple of integers
            valid_tuple (boolean): a private instance attribute

        """
        self.__valid_tuple = False
        self.__position = (0, 0)
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is tuple and len(position) == 2:
            __a, __b = position
            if type(__a) is int and type(__b) is int:
                if __a >= 0 and __b >= 0:
                    self.__position = position
                    self.__valid_tuple = True
        if not self.__valid_tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value
        if type(a) is not int or type(b) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """ user friendly message rep. of the class square """
        user = []
        if self.__size == 0:
            user.append("")
        else:
            for y_pos in range(self.__position[1]):
                user.append("\n")
            for row in range(self.__size):
                for x_pos in range(self.__position[0]):
                    user.append(" ")
                for char_pos in range(self.__size):
                    user.append("#")
                if row != self.__size - 1:
                    user.append("\n")
        return "".join(user)
