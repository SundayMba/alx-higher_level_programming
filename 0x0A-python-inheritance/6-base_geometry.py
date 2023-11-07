#!/usr/bin/python3

"""
    a module that contains a public instance method
"""


class BaseGeometry(object):
    """ Base geometry class with only one method  """
    def area(self):
        raise Exception("area() is not implemented")
