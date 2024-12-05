"""
A program to demonstrate a shallow copy.
"""

import copy

# Create a list.
values = [10]

# Create a copy of the list.
p = copy.copy(values)

# Update the first element in the copy.
p[0] = 5

# Useful for debugging.
pass
