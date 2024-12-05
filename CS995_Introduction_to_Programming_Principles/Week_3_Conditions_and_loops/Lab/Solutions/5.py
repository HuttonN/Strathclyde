"""
Python: Conditions and loops: Q5
"""


number = "3"
try:
    i = int(number)
    i += 10
    print(i)
except ValueError:
    print("The value is not an integer!")
