"""
A program to introduce lists and how to use them.
"""

numbers = [
    4,
    5,
    3
]

# Print all of the values.
print("numbers =", numbers)

# Print the first value.
print("numbers[0] =", numbers[0])

# Print the last value.
print("numbers[-1] =", numbers[-1])

# Access each value, similar to drawing playing cards from a deck.
print("Each of the values:")
for number in numbers:
    print(number)

# Insert 6 between 4 and 5.
numbers = numbers[0:1] + [6] + numbers[1:]

# Print the numbers.
print("Updated numbers =", numbers)
