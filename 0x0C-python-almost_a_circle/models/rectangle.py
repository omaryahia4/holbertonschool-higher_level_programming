#!/usr/bin/python3
""" Module Base """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherited from Parent Class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """

        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Width setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Method that return the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ __str__ method """
        return str("[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height))

    def display(self):
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
