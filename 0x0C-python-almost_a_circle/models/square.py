#!/usr/bin/python3
""" module that models a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that models a square object by inheriting from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor that set up the parent class - rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of the Square object """
        c = "[Square]"
        s = f"{c} ({self.id}) {self.x}/{self.y} - {self.width}"
        return s

    @property
    def size(self):
        """ getter property for size """
        return self.width

    @size.setter
    def size(self, size):
        """ setter property for size """
        if isinstance(size, int):
            if size <= 0:
                raise ValueError("width must be > 0")
            else:
                self.width = size
                self.height = size
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """ update the square method instance """
        if args != ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ convert a square instance to a dictionary """
        d = {}
        d['id'] = self.id
        d['size'] = self.width
        d['x'] = self.x
        d['y'] = self.y
        return d
