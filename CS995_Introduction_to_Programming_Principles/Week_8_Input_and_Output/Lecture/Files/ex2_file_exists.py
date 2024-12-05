import os.path


"""
A program to test if a file exists.
"""
file_name = "my-file.txt"
exists = os.path.isfile("my-file.txt")
if exists:
    print(f"The file \"{file_name}\" exists.")
else:
    print(f"The file \"{file_name}\" does not exist.")
