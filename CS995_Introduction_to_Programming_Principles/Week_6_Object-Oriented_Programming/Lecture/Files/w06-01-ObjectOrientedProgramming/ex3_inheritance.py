"""
A program to demontrate inheritance, where one
class inherits some data members from the
parent class.
"""


class MapPosition:
    def __init__(self):
        self.latitude = 0.
        self.longitude = 0.


class InclinedPosition(MapPosition):
    def __init__(self):
        self.elevation = 0.


m = MapPosition()  # Create a position
m.latitude = 13.0
m.longitude = -10.0
p = InclinedPosition()  # Create an inclined position
p.latitude = 55.860916
p.longitude = -4.251433
p.elevation = 16
