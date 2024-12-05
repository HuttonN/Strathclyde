"""
A program to demonstrate returning and printing
a value.
"""


def return_number():
    """
    A function that returns a number.
    """
    return 10


def print_number():
    """
    A function to print a number.
    """
    print(10)


result = return_number()
print(f"return_number returns {result}")

result = print_number()
print(f"print_number returns {result}")
