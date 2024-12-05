class MyClass:
    """
    A simple class that contains a single private
    data member.
    """
    def __init__(self):
        self.__name = "MyClass"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


"""
A program to demonstrate accessor functions in Python.
Accessor functions (getter and setter) should be avoided
in Python, since they add processing overhead.
"""
m = MyClass()
m.set_name("New name")
print(m.get_name())
