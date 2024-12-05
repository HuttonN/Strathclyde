"""
A program to read a text file and print it.
"""
input_file = open("written-file.txt", "r")
content = input_file.read()  # Read all lines of the file.
content = content.strip()    # Remove trailing new line.
print(content)
input_file.close()
