"""
A program to demonstrate a value error, which
can occur when a string is converted to a number.
"""

c = "123d"

# Attempt to convert the value in c into an integer.
try:
    i = int(c)
except ValueError:
    i = -99

# Print the type and the value of i.
print(type(i), i)
