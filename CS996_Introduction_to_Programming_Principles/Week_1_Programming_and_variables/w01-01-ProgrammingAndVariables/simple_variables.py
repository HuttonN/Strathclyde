"""
A program to demonstrate some simple variable types.
"""

box = 1
box = box + 1
print(box)
text = "The box"
text = text + " contains "
text += str(box)
print(text)
pi = 3.1459
r = 2
area = pi*r*r
print("Radius=" + str(r) + ", area=" + str(area))
