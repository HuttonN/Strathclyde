import copy


class SolarPanel:
    """
    A class to represent a solar panel that is mounted
    on a building.
    """

    def __init__(self, serial_number, power):
        self.serial_number = str(serial_number)
        self.power = power

    def __repr__(self):
        s = "SolarPanel("
        s += f"serial_number=\"{self.serial_number}\","
        s += f"power={self.power})"
        return s


class SolarArray:
    """
    A class to represent a set of solar panels that are
    mounted on the same building.
    """

    def __init__(self, x, y, solar_panels=[]):
        self.x = x
        self.y = y
        self.solar_panels = copy.copy(solar_panels)

    def __repr__(self):
        s = "SolarArray("
        s += f"x={self.x},"
        s += f"y={self.y},"
        s += f"solar_panels={self.solar_panels})"
        return s

    def total_power(self):
        """
        A function to calculate the total power of the solar
        panels that are on this building.
        """

        total = 0.
        for solar_panel in self.solar_panels:
            total += solar_panel.power
        return total


"""
A program to demonstrate the SolarArray and SolarPanel class.
"""
solar_array = SolarArray(12, 13)
solar_array.solar_panels.append(SolarPanel("XXS-213", 10))
solar_array.solar_panels.append(SolarPanel("XYS-233", 9))
new_solar_array = eval(str(solar_array))
print(new_solar_array)
print(solar_array.total_power())
