import unittest
from config_svc import ConfigSvc


class TestConfigSvc(unittest.TestCase):
    def test_load(self):
        config = ConfigSvc("bad_1.json")
        self.assertFalse(config.load())
        config.config_file = "bad_2.json"
        self.assertFalse(config.load())
        config.config_file = "dice_config.json"
        self.assertTrue(config.load())


if __name__ == "__main__":
    unittest.main()
