import math


def safe_sqrt(value_sq):
    """
    A function to return the square root or zero
    when the input value is zero.
    """
    if value_sq < 0:
        raise ValueError("Length is negative.")
    if value_sq == 0:
        return 0
    return math.sqrt(value_sq)


def triangle_side(a=None, b=None, h=None):
    """
    A function to find the length of a side of a right-angle
    triangle given the other two lengths.
    """
    try:
        if a is not None and b is not None and h is None:
            return safe_sqrt(a**2 + b**2)
        if a is None and b is not None and h is not None:
            return safe_sqrt(h**2 - b**2)
        if a is not None and b is None and h is not None:
            return safe_sqrt(h**2 - a**2)
        print("One of the input values must be None.")
    except ValueError as e:
        print(e)
    return None


print(triangle_side(a=3, h=5))
