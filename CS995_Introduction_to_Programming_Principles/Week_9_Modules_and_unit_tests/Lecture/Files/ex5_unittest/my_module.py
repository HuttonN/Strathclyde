def swap(values):
    """
    A function to swap the first and last
    element in a list.
    """
    if not isinstance(values, list):
        raise TypeError("values must be a list.")
    tmp = values[0]
    values[0] = values[-1]
    values[-1] = tmp


"""
A program to demonstrate the swap function.
"""
if __name__ == "__main__":
    numbers = [1, 2]
    swap(numbers)
    print(numbers)
