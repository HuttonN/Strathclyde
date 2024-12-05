"""
Python: Functions: Q4
"""


import random


def fortune():
    """
    A function to provide a random fortune statement.
    """
    statements = [
        "The clouds will part",
        "Next year will be good",
        "Opportunities on the horizon",
        "Something special",
        "Time for fun",
        "An interesting job",
        "Holidays in the future"
    ]
    n = len(statements)
    i = random.randint(0, n-1)
    return statements[i]


print(fortune())
