"""
A program to demonstrate accessing a list element that
does not exist.
"""

values = [
    3
]
print(values[0])

# The program does not reach this line, if the list
# index at line 9 is out of range.
print("Next")

# Catch the list index being out of range.
try:
    print(values[1])
except IndexError:
    print("Out of range!!")
