"""
A program to demonstrate how mutable variables
behave when passed to a function.
"""


def fun(my_values):
    """
    A function to append a value to an input list.
    """
    my_values.append(7)


# Define an empty list.
values = []

# Call the function.
fun(values)

# Useful for debugging.
pass
