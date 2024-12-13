# Worked Examples

# Lecture Notes: Advanced Python Programming Examples

## Overview

This lecture explores advanced Python programming concepts through detailed examples:
- JSON parsing with file operations.
- Implementing and testing file-based parsers.
- Creating mock configurations for testing in complex scenarios.

We revisit key ideas from earlier lectures, applying them to build and test practical examples.

---

## Example 1: JSON Parser with Files

### `network.py`

Code:

```python
import json


class NetworkedDevice:
    """
    A class to represent a device on a computer network.
    """
    def __init__(self,
                 mac_address="",
                 ip_address="",
                 os=""):
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.os = os

    def __repr__(self):
        s = "NetworkedDevice("
        s += f"mac_address=\"{self.mac_address}\","
        s += f"ip_address=\"{self.ip_address}\","
        s += f"os=\"{self.os}\""
        s += ")"
        return s

    def from_json(self, json_str):
    """
    A function to populate the data members with data
    taken from an input JSON string.
    """
    try:
        # Attempt to parse the input string as JSON. loads() converts JSON to a dictionary
        json_data = json.loads(json_str)
    except TypeError as exception:
        # Handle the case where the input is not a valid JSON string
        print(exception)  # Print the error message for debugging
        return False  # Indicate failure to parse JSON

    # Check if the parsed JSON data is a dictionary
    if not isinstance(json_data, dict):
        print("Error: The JSON string must contain a dictionary.")
        return False  # Indicate failure because the JSON isn't in the expected format

    try:
        # Extract and assign values from the dictionary to class attributes
        # Cast each value to a string to ensure type consistency
        self.mac_address = str(json_data["mac_address"])
        self.ip_address = str(json_data["ip_address"])
        self.os = str(json_data["os"])
    except KeyError as exception:
        # Handle missing keys in the dictionary
        msg = f"Error: The key {exception} is not found"
        msg += " in the input JSON string."
        print(msg)  # Print a specific error message
        return False  # Indicate failure due to missing expected keys
    except ValueError as exception:
        # Handle cases where the values cannot be cast to strings
        print(exception)  # Print the error message for debugging
        return False  # Indicate failure to cast a value to the expected type

    # Return True to indicate that the operation was successful
    return True

    def to_json(self):
        """
        A function to return a JSON string that contains
        values from the data members.
        """
        json_data = {
            "mac_address": self.mac_address,
            "ip_address": self.ip_address,
            "os": self.os
        }
        json_str = json.dumps(json_data)
        return json_str
```

#### **Class: `NetworkedDevice`**
A class representing a networked device with:
- `mac_address` (str): The MAC address.
- `ip_address` (str): The IP address.
- `os` (str): The operating system.

##### **Methods**
1. `__init__`: Initializes the object with three parameters.
2. `__repr__`: Converts the object into a string for recreating it via `eval`.
3. `from_json`: Populates object attributes from a JSON string. Handles:
   - `TypeError`: Invalid JSON input.
   - `KeyError`: Missing keys.
   - `ValueError`: Unexpected value types.
4. `to_json`: Converts object attributes into a JSON string.

#### **Code Example**
```python
device = NetworkedDevice(
    mac_address="b8:27:eb:4f:15:96",
    ip_address="192.168.1.4",
    os="Linux"
)
json_str = device.to_json()
print(json_str)
```

### `test_network.py`

Code:

```python
import unittest
from network import NetworkedDevice


class TestNetworkedDevice(unittest.TestCase):
    def test_repr(self):
        # create a test device
        device = NetworkedDevice(
            mac_address="b8:27:eb:4f:15:96",
            ip_address="192.168.1.4",
            os="Linux"
        )
        new_device = eval(str(device)) # creates new instance of NetworkedDevice using eval
        self.assertEqual(device.mac_address, new_device.mac_address) 
        self.assertEqual(device.ip_address, new_device.ip_address)
        self.assertEqual(device.os, new_device.os)

    def test_json_parsing(self):
        # create a test device
        device = NetworkedDevice(
            mac_address="b8:27:eb:4f:15:96",
            ip_address="192.168.1.4",
            os="Linux"
        )
        json_str = device.to_json() #creates JSON text string
        new_device = NetworkedDevice() #creates new object with default values
        self.assertTrue(new_device.from_json(json_str)) #reads JSON string to new_device
        self.assertEqual(device.mac_address, new_device.mac_address)
        self.assertEqual(device.ip_address, new_device.ip_address)
        self.assertEqual(device.os, new_device.os)

        # Test the exception types.
        self.assertFalse(new_device.from_json([]))
        self.assertFalse(new_device.from_json("[]"))
        self.assertFalse(new_device.from_json("{}"))


if __name__ == "__main__":
    unittest.main()
```
