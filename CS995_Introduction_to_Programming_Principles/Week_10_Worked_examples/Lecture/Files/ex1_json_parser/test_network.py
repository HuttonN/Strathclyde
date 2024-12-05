import unittest
from network import NetworkedDevice


class TestNetworkedDevice(unittest.TestCase):
    def test_repr(self):
        device = NetworkedDevice(
            mac_address="b8:27:eb:4f:15:96",
            ip_address="192.168.1.4",
            os="Linux"
        )
        new_device = eval(str(device))
        self.assertEqual(device.mac_address, new_device.mac_address)
        self.assertEqual(device.ip_address, new_device.ip_address)
        self.assertEqual(device.os, new_device.os)

    def test_json_parsing(self):
        device = NetworkedDevice(
            mac_address="b8:27:eb:4f:15:96",
            ip_address="192.168.1.4",
            os="Linux"
        )
        json_str = device.to_json()
        new_device = NetworkedDevice()
        self.assertTrue(new_device.from_json(json_str))
        self.assertEqual(device.mac_address, new_device.mac_address)
        self.assertEqual(device.ip_address, new_device.ip_address)
        self.assertEqual(device.os, new_device.os)

        # Test the exception types.
        self.assertFalse(new_device.from_json([]))
        self.assertFalse(new_device.from_json("[]"))
        self.assertFalse(new_device.from_json("{}"))


if __name__ == "__main__":
    unittest.main()
