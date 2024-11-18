"""
A program to demonstrate how immutable variables
behave when passed to a function.
"""


def fun(x, y):
    """
    A function to assign values to variables.
    """
    x = 12
    y = 4


# Create two values and assign them values.
k = 10
p = 3

# Call the function.
fun(k, p)

# Useful for debugging.
pass
