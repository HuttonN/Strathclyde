def print_list(lst):
    """
    A function to recursively unpack an input
    list that might contain other lists.
    """
    for value in lst:
        if isinstance(value, list):
            print_list(value)
        else:
            print(value)


"""
A program to create a list of lists and unpack it.
"""
input_list = [
    [2, 3],
    [4, 5]
]
print_list(input_list)
