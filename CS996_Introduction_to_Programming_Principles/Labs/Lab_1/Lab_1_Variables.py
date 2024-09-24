"""
1. Write a program that includes two integer variables. Create a third integer variable by assigning it the
result of multiplying the first two variables. The program should print the value of all three variables.

"""

#Solution

a = 2
b = 3
c = a*b
print(c)

"""
2. Write a program that contains a list that contains several numbers as separate elements. Print the contents
of the list, sort the list and then print the list again.

"""

list_1 = [ 
    4,
    9,
    2
]

print(list_1)

list_1.sort

print(list_1)

"""
3. Write a program that contains a floating point variable, which is the radius of a circle. The program should
use the math library to calculate the area of the circle. The area of the circle is given by:

a = πr2

where a is the area, π is available in the math library as math.pi and r is the radius. The square of a r can
be calculating by using math.pow(r,2) or r**2. The program should print the radius and the area.

"""
#radius = 2.16
#Area = math.pi

"""
4. Write a program that contains a dictionary of author names and citations. The key should be the author
name and the values should be the number of citations. Print out the citations for two of the authors.

"""

author_dict = {
    "jiminy jimmers": 2,
    "hummana hummana": 1
}

print(author_dict.values())

"""
5. Write a program that contains two integer variables, where the first one contains 3 and the second one
contains 2. Divide the first variable by the second variable and assign the result to a new variable. Check
the type of the third variable by using print(type(result)), where result contains the result of the
division.

"""

var_1 = 3
var_2 = 2
var_3 = var_1/var_2
print(type(var_3))

"""
6. Write a program that contains two string variables. Print the first two characters of the first string variable.
Create a new string variable by combining the first two characters from the first string variable with the first
two characters from the second variable. Print the values of the three string variables.

"""

str_var1 = "Hello"
str_var2 = "there"
str_var3 = str_var1[0:2] + str_var2[0:2]
print(str_var3)

"""
7. Write a program that contains an integer variable and a string variable. Use the str function to cast the
value of the integer variable to a string. Then append the string version of the integer variable to the string
variable and print the result.
"""

str_var4 = "Happy"
int_var = 3
str_var5 = str(int_var)
str_var6 = str_var4 + str_var5
print(str_var6)

"""
8. Write a program that contains a string variable and a floating point variable. Store "2.5" in the string
variable. Use the float function to cast the string variable to a float. Then add the float value of the string
variable to the float variable. Print the result of the addition and the contents of the two input variables.
"""

str_var7 = "2.5"

"""
9. Write a program that contains a string variable. Store "2n" in the string variable. Use the int function to
attempt to cast the string value to an integer. Comment on what happens.
"""

#str_var7 = "2n"
#int(str_var7)

#The following error message is printed: "ValueError: invalid literal for int() with base 10: '2n' "

"""
10. Write a program that contains a list, which contains two elements that are also lists. Then print the
contents of the list
"""

list_var = [[1,2,3], [3,2,1]]
print(list_var)

"""
11. Write a program that contains a dictionary, which contains two key and value pairs, where the values are
lists. Then print the contents of the dictionary.
"""

dict_lists = {
    "list1": [4,2,0],
    "list2": [0,2,4]
}

print(dict_lists)

"""
12. Write a program that contains a dictionary. Then try to get a value, using a key that does not exist.
Comment on what happens.
"""

dict_1 = {
    "entry1": 34,
    "entry2": "string"
}

#print(dict_1["entry3"])

# The following error message is displayed: "KeyError: 'entry3'"

"""
13. Write a program that contains a list. Try to access a list element, using an index that does not exist in the
list. Comment on what happens.
"""

list_1 = [
     4,
     2,
     3
]

# print(list_1[6])

# The following error message is displayed: "IndexError: list index out of range"