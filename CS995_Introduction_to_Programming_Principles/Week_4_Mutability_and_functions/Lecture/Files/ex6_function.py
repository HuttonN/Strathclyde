"""
A function to demonstrate global variables.
"""

# This variable is defined outside of the function.
g = 10


def fun(x, y):
    """
    A function to add two numbers together and assign
    them to a global variable.
    """

    # Need to state that g is the global variable.
    global g

    # Update the value in g.
    g = x + y


# Call the function.
r = fun(10, 3)

# Useful for debugging.
pass
