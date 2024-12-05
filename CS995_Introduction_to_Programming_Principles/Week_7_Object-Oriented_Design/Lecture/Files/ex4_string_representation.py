class MyClass:
    """
    A simple class that contains a single data member.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyClass(name=\"{self.name}\")"


"""
A program that demonstrates the conversion of an object
to a text string, using the repr function.
"""

# Create an object.
obj = MyClass("Some name")

# Print an object, which causes the object to be coverted
# to a string.
print(obj)

# Use eval to run the text through the Python interpreter.
obj2 = eval(str(obj))
