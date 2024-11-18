"""
A program to demonstrate a deep copy.
"""

import copy

# Create a list that contains a list,
# which contains a single value.
values = [[10]]

# Perform a deep copy, copying the internal
# list too.
p = copy.deepcopy(values)

# Update the first value that is in the list.
p[0][0] = 5

# Useful for debugging.
pass
