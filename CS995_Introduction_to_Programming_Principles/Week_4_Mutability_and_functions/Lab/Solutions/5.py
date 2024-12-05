"""
Python: Functions: Q5
"""


def fill_dict(values):
    """
    A function to clear an input dictionary and add three values to it.
    """
    values.clear()
    values["a"] = 1
    values["b"] = 2
    values["c"] = 3


input_values = {
    "zz": 100
}
print(input_values)
fill_dict(input_values)
print(input_values)
