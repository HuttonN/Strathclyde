import unittest
import solar_array


class TestSolarArray(unittest.TestCase):
    def test_total_power(self):
        array = solar_array.SolarArray(12, 13)
        array.solar_panels.append(solar_array.SolarPanel("XXS-213", 10))
        array.solar_panels.append(solar_array.SolarPanel("XYS-233", 9))
        self.assertEqual(array.total_power(), 19)


if __name__ == '__main__':
    unittest.main()
