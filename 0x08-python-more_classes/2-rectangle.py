#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """ class Rectangle """
    def __init__(self, width=0, height=0):
        """
            Init Rectangle Class
            Args:
                width (int): The width of rectangle
                height (int): Thhe height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height

    @property
    def width(self):
        """
            width getter
            Return: The width of the Rectangle (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width setter
            Args:
                Value (int) : a value to set
            Raises:
                TypeError: When value is not int
                ValueError: When value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    def area(self):
        """
            Return Rectangle Area
            Return: rectangle area
        """
        area = (self.width * self.height)
        return area

    def perimeter(self):
        """
            Return the perimeter of rectangle
            Return : rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            perimeter = 0
        sum = (self.width + self.height)
        perimeter = 2 * sum
        return perimeter