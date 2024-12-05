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
        that are taken from an input JSON string.
        """
        try:
            json_data = json.loads(json_str)
        except TypeError as exception:
            print(exception)
            return False
        if not isinstance(json_data, dict):
            print("Error: The JSON string must contain a dictionary.")
            return False
        try:
            self.mac_address = str(json_data["mac_address"])
            self.ip_address = str(json_data["ip_address"])
            self.os = str(json_data["os"])
        except KeyError as exception:
            msg = f"Error: The key {exception} is not found"
            msg += " in the input JSON string."
            print(msg)
            return False
        except ValueError as exception:
            print(exception)
            return False
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
