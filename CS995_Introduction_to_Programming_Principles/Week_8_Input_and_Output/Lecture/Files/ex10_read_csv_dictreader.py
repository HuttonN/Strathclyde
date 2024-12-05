import csv


"""
A program to read a CSV file, using
the CSV DictReader.
"""
input_file = open("test.csv")
dict_reader = csv.DictReader(input_file)
for row in dict_reader:
    print(row)
input_file.close()
