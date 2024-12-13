"""
Write a program that converts the string values "one", "two", "three", "four", "five", "six", "seven",
"eight" and "nine" into the corresponding integer value. For example, the program should print 1, when
a string variable contains "one". The program should use a dictionary to solve this problem and check if
the string is a dictionary key before using it to lookup the value.
"""

values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

number = "six"
if number in values.keys():
    print(values[number])