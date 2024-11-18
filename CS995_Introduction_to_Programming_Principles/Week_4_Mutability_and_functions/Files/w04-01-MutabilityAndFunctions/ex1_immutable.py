"""
A program to demonstrate the nature of a immutable variable.
The program can be run using the debugger to verify when
the value in x and y is updated.
"""

# Create a variable and assign 10.
x = 10

# Copy the value from x to y.
y = x

# Update the value in y.
y = 5

# Update the value in x, using the value in y.
x = y

# Useful for breakpoints.
pass
