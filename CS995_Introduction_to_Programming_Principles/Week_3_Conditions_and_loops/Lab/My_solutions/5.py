"""Write a program that converts a string into an integer, by casting the string to an integer. If the string is not
an integer, then the program should print an error message. If the string is an integer, then the program
should add 10 to the integer value and print it.

The function should use try and except to catch the ValueError exception that is thrown if the string is
not an integer."""

# Input: string from the user
user_input = input("Enter a number: ")

try:
    # Try to convert the string to an integer
    number = int(user_input)
    # Add 10 to the integer and print the result
    print(f"The result is: {number + 10}")
except ValueError:
    # If conversion fails, print an error message
    print("Error: The input is not a valid integer.")

