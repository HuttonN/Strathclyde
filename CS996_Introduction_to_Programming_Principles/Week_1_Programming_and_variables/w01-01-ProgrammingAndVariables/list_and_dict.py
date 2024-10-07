"""
A Program to demonstrate that lists and dictionaries can
contain other lists and dictionaries.
"""

# A list that contains lists as elements.
numbers = [[1, 3], [4]]

# Print the second element in the first list.
print(numbers[0][1])

# Define a dictionary that contains a list.
values = {
    10: [
        1,
        3
    ]
}

# Print the contents of the dictionary.
print(values)
