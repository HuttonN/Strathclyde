"""
A program to demonstrate one for loop nested inside
another one, together with break.
"""

for i in range(4, 6):
    if i == 5:
        break
    for j in range(3):
        print(i*j)
