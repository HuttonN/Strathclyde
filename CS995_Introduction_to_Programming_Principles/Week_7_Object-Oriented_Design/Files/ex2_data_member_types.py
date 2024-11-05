class MyClass:
    """
    A simple class to demonstrate public, private and
    protected data members.
    """
    def __init__(self):
        self.name = "MyClass"
        self._protected_name = "Only derived know"
        self.__private_name = "Only this class knows"

    def public_function(self):
        return "This a public function"

    def _protected_function(self):
        return "This is a protected function"

    def __private_function(self):
        return "This is a private function"


# Create an object.
o = MyClass()

# Get the value of a public data member.
print(o.name)

# Get the value of a private data member.
# (This will fail.)
print(o.__private_name)
