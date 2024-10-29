"""
A program that includes a class with a
single member function.
"""


class MyClass:
    def __init__(self):
        self.name = "MyClass"

    def full_name(self):
        return self.name + " is an example"


m = MyClass()
m.name = "New name"
print("full_name = " + m.full_name())
