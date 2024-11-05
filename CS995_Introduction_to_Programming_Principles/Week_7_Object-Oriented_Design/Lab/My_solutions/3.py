"""Write a __repr__(self) function for the SolarArray and SolarPanel class, which should return the string
representation of the objects. The function should allow a new object to be created by using eval on the
returned string."""

class SolarPanel:
    """
    A class to represent a solar panel that is mounted
    on a building.
    """

    def __init__(self, serial_number, power):
        self.serial_number = str(serial_number)
        self.power = power

    def __repr__(self):
        return f"SolarPanel({self.serial_number}, {self.power})"


class SolarArray:
    """
    A class to represent a set of solar panels that are
    mounted on the same building.
    """

    def __init__(self, x, y, solar_panels=[]):
        self.x = x
        self.y = y
        self.solar_panels = copy.copy(solar_panels)

    def total_power(self):
        """
        A function to calculate the total power of the solar
        panels that are on this building.
        """

        total = 0.
        for solar_panel in self.solar_panels:
            total += solar_panel.power
        return total
    
    def __repr__(self):
        return f"SolarArray({self.x}, {self.y}, {self.solar_panels})"
    
solar_panel1 = SolarPanel (1112, 1000)
print(solar_panel1)
solar_panel2 = eval(str(solar_panel1))
print(solar_panel2)

