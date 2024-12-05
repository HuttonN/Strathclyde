class DataElement:
    """
    A class that is described using UML in the discussion.
    """
    def __init__(self):
        self.public_data = 10
        self._protected_data = "A string"
        self.__private_data = True

    def multiply_numbers(self, x=3):
        return 0.

    def test_something(self):
        return False
