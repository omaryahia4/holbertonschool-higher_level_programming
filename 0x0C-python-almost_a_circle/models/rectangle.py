#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): x
            y(int): y
            id(int): id inherited from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


    def area(self):
        """ Method that return the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """ The display function """
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute"""

        if args:
            for arg, val in enumerate(args):
                if arg == 0:
                    self.id = val
                if arg == 1:
                    self.width = val
                if arg == 2:
                    self.height = val
                if arg == 3:
                    self.x = val
                if arg == 4:
                    self.y = val
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary Representation of Rectangle class """
        dict = {}
        dict["id"] = self.id
        dict["height"] = self.height
        dict["width"] = self.width
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
