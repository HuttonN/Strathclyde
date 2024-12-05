class MapPosition:
    """
    A class to hold map position information.
    """
    def __init__(self):
        self.latitude = 0.
        self.longitude = 0.


class InclinedPosition(MapPosition):
    """
    A class to hold a map position and inclination.
    """
    def __init__(self):
        self.elevation = 0.


"""
A program to demonstrate inheritance of data members.
"""

# Create a position
m = MapPosition()
m.latitude = 13.0
m.longitude = -10.0

# Create an inclined position
p = InclinedPosition()
p.latitude = 55.860916
p.longitude = -4.251433
p.elevation = 16
