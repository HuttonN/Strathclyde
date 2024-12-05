import json
import os


class ConfigSvc:
    """
    A class to hold configuration data that is loaded from
    an associated configuration file.
    """
    def __init__(self,
                 config_file):
        self.config_file = config_file
        self.__config_data = None

    def config(self):
        """
        A function to return the configuration data.
        """
        if self.__config_data is None:
            success = self.load()
            if not success:
                self.__config_data = None
        return self.__config_data

    def load(self):
        """
        A function to load the configuration data from a
        JSON file.
        """
        if not os.path.isfile(self.config_file):
            print(f"Cannot find file \"{self.config_file}\".")
            return False
        input_file = open(self.config_file, "r", encoding="utf8")
        file_contents = input_file.read()
        input_file.close()

        # Attempt to read the text as JSON.
        try:
            self.__config_data = json.loads(file_contents)
        except json.JSONDecodeError as e:
            print(f"Error when decoding \"{self.config_file}\".")
            print(e)
            return False
        except TypeError as e:
            print(f"Error when decoding \"{self.config_file}\".")
            print(e)
            return False
        return True
