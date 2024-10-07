"""

A program to introduce Python

"""

print("Well hello there!")

"""
Simple variables
"""

box = 1
box = box + 1
print(box)

text = "the box"
text = text + " contains "
text += str(box)
print(text)

pi = 3.1459
r = 2
area = pi*r*r
print("Radius=" +str(r))

"""
Basic containers: Lists
"""

numbers = [
    4,
    5,
    3
]
print("numbers = ", numbers)
print("numbers[0] =", numbers[0])
print("numbers[-1] =", numbers[-1])
print("Each of the values:")
for number in numbers:
    print(number)
numbers = numbers[0:1] + [6] +numbers[1:]

"""
Basic containers: Lists
"""

values = {
    "a":5,
    "b":6
}
values["c"] = 15
values["b"] = 10
values.update({
    "d": 20,
    "e": 9
})
print(values)
print(values["d"])