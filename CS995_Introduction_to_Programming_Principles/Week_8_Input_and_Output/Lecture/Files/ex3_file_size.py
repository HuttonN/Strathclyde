import os.path


"""
A program to get the size of a file.
"""
file_name = "my-file.json"
file_size = os.path.getsize(file_name)
print(f"{file_name} is {file_size} bytes.")
