#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class.
"""


class Rectangle:
    """A simple Rectangle class"""
    def __init__(self,width=0, height = 0) -> None:
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return (self.__width)
    
    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError
        elif value < 0:
            raise ValueError
        
    @property
    def height(self):
        return (self.__height)
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError
        elif value < 0:
            raise ValueError