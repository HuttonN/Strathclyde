"""1. Create a class to represent an electric car.
• The class should include data members for the speed, map coordinates (x and y), electric charge
and maximum charge.
• Write a function to return the percentage electric charge, using the electric charge and the maximum
electric charge."""

class ElectricCar:
    def __init__(self, speed, x, y, electric_charge, max_charge):
        self.speed = speed
        self.x = x
        self.y = y
        self.electric_charge = electric_charge
        self.max_charge = max_charge

    def charge_percentage(self):
        if self.electric_charge > 0:
            return (self.electric_charge/self.max_charge) * 100
        return 0