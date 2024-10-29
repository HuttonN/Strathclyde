"""2. A house has a solar panel array on it that is controlled by a small computer system that is part of the solar array installation.
• Define a SolarPanel class that includes a public data member to hold a serial number as a text string
and a public data member to hold the power produced as a floating point value.
• Define a SolarArray class that contains a public data member that is a list of solar panel objects, and
map coordinates (x and y) for the solar array. The constructor should have three input parameters:
d e f__i n i t__( s e l f , x , y , s o l a r _ p a n e l s = [ ] ) :
The constructor should use a shallow copy to copy the input solar_panels to a data member.
• Add a member function to the SolarArray class that returns the total power of the solar array, by
looping over the SolarPanel objects and summing their power values."""

class SolarPanel:
    def __init__(self, serial_number, power):
        self.serial_number = serial_number
        self.power = power

class SolarArray:
    def __init__(self, x, y, solar_panels = []):
        self.x = x
        self.y = y
        self.solar_panels = list(solar_panels)

    def total_power(self):
        return sum (panel.power for panel in self.solar_panels)