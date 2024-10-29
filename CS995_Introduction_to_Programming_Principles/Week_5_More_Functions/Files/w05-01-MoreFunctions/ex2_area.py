import math


def area_of_square(length):
    """
    A function to calculate the area of a
    square, using the input length.
    """
    return length**2


def area_of_circle(radius):
    """
    A function to calculate the area of a
    circle, using the input radius.
    """
    return math.pi*(radius**2)


"""
A program to compare the area of a circle and
square.
"""
print(area_of_circle(0.5))
print(area_of_square(1))
