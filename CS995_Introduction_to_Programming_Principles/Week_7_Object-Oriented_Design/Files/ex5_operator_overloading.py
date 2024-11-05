class DataClass:
    """
    A simple class that contains one data member.
    """
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return not self.__eq__(other)


"""
A program to demonstrate operator overloading, using
the equal and not equal operators.
"""
d = DataClass(10)
p = DataClass(10)
print("d == p : " + str(d == p))
print("d != p : " + str(d != p))
