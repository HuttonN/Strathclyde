"""1. Create a class to represent an electric car.
• The class should include data members for the speed, map coordinates (x and y), electric charge
and maximum charge.
• Write a function to return the percentage electric charge, using the electric charge and the maximum
electric charge."""

class ElectricCar:
    """
    Class to represent an electric car
    """

    def __init__(self, speed, x, y, charge, max_charge):
        self.speed = speed
        self.x = x
        self.y = y
        self.charge = charge
        self.max_charge = max_charge

    def percentage_charge(self):
        """
        A function to return the percentage charge.
        """

        if self.max_charge == 0:
            return 0
        return self.charge/self.max_charge*100
    
"""
A test program to demonstrate the ElectricCar class
"""

car = ElectricCar(10, 50, 20, 150, 1000)
print(car.percentage_charge())