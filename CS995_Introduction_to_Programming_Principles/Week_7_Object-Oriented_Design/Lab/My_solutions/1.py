"""Write a __repr__(self) function for the ElectricCar class, which should return a string representation
of the object. The function should allow a new object to be created by using eval on the returned string:
car = ElectricCar (10 , 50, 20, 150 , 1000)
new_car = eval ( str ( car ))"""

class ElectricCar:
    """
    A class to represent an electric car.
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
    
    def __repr__(self):
        return f"ElectricCar({self.speed}, {self.x}, {self.y}, {self.charge}, {self.max_charge})"

car = ElectricCar (10, 50, 20, 150, 1000)
print(car)

new_car = eval(str(car))
print(new_car)