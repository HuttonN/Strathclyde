"""Write a program that includes a function that appends two values to a list. The function should not return
the list, but accept the list to be updated as an input parameter. The program should print the list after the
function has been called."""

# function definition
def append_to_list(my_list, num1, num2):
    my_list.append(num1)
    my_list.append(num2)

# main program

# original list
my_list = [1,2,3]
print(f"Original list: {my_list}")

# updating list
append_to_list(my_list,4,5)

# Updated list
print(f"Updated list: {my_list}")