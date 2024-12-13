"""
Write a program that contains two string variables. Print the
first two characters of the first string variable. Create a
new string variable by combining the first two characters from
the first string variable with the first two characters from
the second variable. Print the values of the three string variables.
"""

string_1 = "Easy buddy"
string_2 = "I'm closeted"

print(string_1[0:2])

string_3 = string_1[0:2] + string_2[0:2]

print(string_1)
print(string_2)
print(string_3)