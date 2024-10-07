"""
A program to demonstrate using a dictionary key
that does not exist.
"""

d = {
    1: 24
}

# Trying to use a key that does not exist.
try:
    print(d[2])
except KeyError:
    print("Out of range!!")
