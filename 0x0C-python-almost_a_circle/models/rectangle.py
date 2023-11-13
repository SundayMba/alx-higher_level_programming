#!/usr/bin/python3
""" Subclass module for Base implementing Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Subclass for Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle constructor

            this class has 4 private attribute and 4 public getter and setter
            property.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter property """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter property """
        if isinstance(width, int):
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Getter property for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter property for height """
        if isinstance(height, int):
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ Getter property for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter property for x """
        if isinstance(x, int):
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ Getter property for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter property for y """
        if isinstance(y, int):
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ calculate rectangle area """
        return self.width * self.height

    def display(self):
        """ Display rectangle in stdout using # """
        """ y-position """
        for y_pos in range(self.y):
            print()
        for row in range(self.height):
            for x_pos in range(self.x):
                print(' ', end='')
            for col in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """ string representation of the instance """
        cls = "[Rectangle]"
        s = f"{cls} ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return s

    def update(self, *argv, **kwargs):
        """ a pointer to a variable number of positional arguments """
        if argv != ():
            if len(argv) >= 1:
                self.id = argv[0]
            if len(argv) >= 2:
                self.width = argv[1]
            if len(argv) >= 3:
                self.height = argv[2]
            if len(argv) >= 4:
                self.x = argv[3]
            if len(argv) >= 5:
                self.y = argv[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ build and a dictionary using the instance attribute """
        d = {}
        d['id'] = self.id
        d['width'] = self.width
        d['height'] = self.height
        d['x'] = self.x
        d['y'] = self.y
        return d
