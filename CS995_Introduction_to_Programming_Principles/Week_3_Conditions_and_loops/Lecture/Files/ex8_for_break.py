"""
A program to demonstrate break within a for loop.
"""


numbers = [2, 4, 5]
for number in numbers:
    if number > 4:
        break
    print(number)
print("Finished")
