"""
A program to write a text file.
"""
output_file = open("written-file.txt", "w")
output_file.write("A text string" + "\n")
output_file.close()
