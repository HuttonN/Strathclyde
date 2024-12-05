import math
import unittest
from simulate_dice import check_config, average_dice_total


class MockConfigSvc:
    """
    A mock version of the ConfigSvc class to support testing.
    """
    def __init__(self,
                 config_file):
        self.config_file = config_file
        self.__config_data = None

    def set_config_data(self, config_data):
        self.__config_data = config_data

    def config(self):
        return self.__config_data

    def load(self):
        return True


class TestSimulateDice(unittest.TestCase):
    """
    A class to test functions defined in simulate_dice.
    """
    def test_check_config(self):
        config = MockConfigSvc("None")
        config.set_config_data({
            "dice": [
                {
                    "n_sides": 6
                },
                {
                    "n_sides": 0.5
                }
            ],
            "n_rolls": 10000
        })
        self.assertFalse(check_config(config))

    def test_simulate(self):
        config = MockConfigSvc("None")
        config.set_config_data({
            "dice": [
                {
                    "n_sides": 6
                },
                {
                    "n_sides": 6
                }
            ],
            "n_rolls": 10000
        })
        average = average_dice_total(config)
        self.assertTrue(math.isclose(average, 7.0, rel_tol=0.1))


if __name__ == "__main__":
    unittest.main()
