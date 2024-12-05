def count_names(input_list, counts):
    """
    A function to count the number of times a
    word appears in a list.  The results are
    recorded in the dictionary counts.
    """
    counts.clear()
    for value in input_list:
        if value not in counts.keys():
            counts[value] = 0
        counts[value] += 1


"""
A program to count words in a list.
"""
shopping_basket = [
    "apple",
    "pear",
    "apple",
    "apple"
]
counts = {}
count_names(shopping_basket, counts)
print(f"The basket contains: {counts}")
