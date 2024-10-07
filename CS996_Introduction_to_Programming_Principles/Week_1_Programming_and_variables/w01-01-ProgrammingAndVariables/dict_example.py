"""
A program to demonstrate declaring and using a dictionary.
"""

values = {
    "a": 5,
    "b": 6
}
values["c"] = 15
values["b"] = 10
values.update({
    "d": 20,
    "e": 9
})
print(values)
print(values["d"])
