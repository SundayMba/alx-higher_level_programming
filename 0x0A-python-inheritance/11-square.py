#!/usr/bin/python3

"""
    a module that contains a public instance method
"""


bg = __import__('9-rectangle').Rectangle
""" importation of Base Rectangle class """


class Square(bg):
    """ Base rectangle class with only one method  """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        """constructor"""

    def __str__(self):
        """ string implementation of the instance """
        return f"[Square] {self.__size}/{self.__size}"
