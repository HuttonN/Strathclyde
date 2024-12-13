"""
Write a program that contains an integer variable. Write a for loop that starts from 1 and 
continues to the value of the integer variable + 1. Multiply each of the numbers together. 
Print the result of the multiplication.
"""

my_int = 567

product = 1
for integer in range(1,my_int+1):
    product *= integer

print(product)