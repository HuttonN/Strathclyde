import math


class Cube:
    """
    A class to represent the properties of a cube.
    """

    def __init__(self, length):
        self.length = length

    def volume(self):
        """
        A function to return the volume of the cube.
        """
        return math.pow(self.length, 3)


"""
A program to create a cube and calculate its volume.
"""
cube = Cube(2)
v = cube.volume()

# Useful for debugging.
pass
