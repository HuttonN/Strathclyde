import unittest
import electric_car


class TestElectricCar(unittest.TestCase):
    def test_percentage_charge(self):
        car = electric_car.ElectricCar(10, 50, 20, 150, 1000)
        self.assertEqual(car.percentage_charge(), 15)


if __name__ == '__main__':
    unittest.main()
