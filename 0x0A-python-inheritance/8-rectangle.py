#!/usr/bin/python3

"""defines a class Rectangle that inherits from  BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using basegeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle
        Args:
            width (int): width of the new Rectangle
            height (int): height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
