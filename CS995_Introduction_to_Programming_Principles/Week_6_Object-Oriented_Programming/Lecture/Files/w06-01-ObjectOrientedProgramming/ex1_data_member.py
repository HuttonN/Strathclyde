"""
A program that includes a class with a
single data member.
"""


class MyClass:
    def __init__(self, name):
        self.name = name


m1 = MyClass("A new object")
m2 = MyClass("A new object")
m1.name = "Updated name"
print("m1.name = " + m1.name)
print("m2.name = " + m2.name)
