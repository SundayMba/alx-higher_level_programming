#!/usr/bin/python3

"""
    a module that contains a public instance method
"""


class BaseGeometry(object):
    """ Base geometry class with only one method  """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate an integer """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
