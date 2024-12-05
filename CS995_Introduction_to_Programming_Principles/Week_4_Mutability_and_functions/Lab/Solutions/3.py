"""
Python: Functions: Q3
"""


import random


def roll_dice(n_dice, n_sides):
    """
    A function to simulate rolling one or more dice.  The function returns the
    total value from rolling the dice.
    """
    sum = 0
    for _ in range(n_dice):
        sum += random.randint(1, n_sides)
    return sum


n_dice = 3
n_sides = 6
sum = roll_dice(n_dice, n_sides)
print(f"n_dice={n_dice}, n_sides={n_sides}, sum={sum}")
