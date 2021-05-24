#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """ class Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Init Rectangle Class
            Args:
                width (int): The width of rectangle
                height (int): The height of rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
            height getter
            Return: the height of the rectangle (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
            Args:
                value (int) : value to be set
            Raises:
                TypeError: When value is not int
                ValueError: When value is less than 0
        """
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
            Return: (int) rectangle area
        """
        area = (self.__width * self.__height)
        return area

    def perimeter(self):
        """
            Return the perimeter of rectangle
            Return : (int) rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        sum = (self.__width + self.__height)
        perimeter = 2 * sum
        return perimeter

    def __str__(self):
        """
            print the rectangle in '#' character
        Return:
            rectangle of '#'
            """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += str(self.print_symbol)
            if i < self.__height - 1:
                my_str += "\n"
        return my_str

    def __repr__(self):
        """
            string representation of the rectangle
            Return:
            (str) representation of the rectangle
        """
        return("Rectangle ({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print ("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
            compares between 2 rectangles
            Args:
                rect_1: First Rectangle
                rect_2: Second Rectangle
            Raises:
                TypeError: If rect_1 is not instance of Rectangle
                TypeError: If rect_2 is not instance of rectangle
            Return:
                The biggest Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
