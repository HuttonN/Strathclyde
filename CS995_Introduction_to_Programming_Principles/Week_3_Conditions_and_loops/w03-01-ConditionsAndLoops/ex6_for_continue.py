"""
A program to demonstrate continue within a for loop.
The program only prints 2 and 5, skipping 4.
"""


numbers = [2, 4, 5]
for number in numbers:
    if number == 4:
        # Some other logic..
        continue
    print(number)
