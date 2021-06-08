#!/usr/bin/python3
""" Module square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ method """
        return str("[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Size getter """
        return self.width and self.height

    @size.setter
    def size(self, size):
        """ Size setter """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute"""
        if args:
            for arg, val in enumerate(args):
                if arg == 0:
                    self.id = val
                if arg == 1:
                    self.size = val
                if arg == 2:
                    self.x = val
                if arg == 3:
                    self.y = val
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary Representation of Square class """
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
