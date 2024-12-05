import csv


"""
A program to read a CSV file, using
the CSV reader.
"""
input_file = open("my-file.csv", "r", newline='')
csv_reader = csv.reader(input_file, delimiter=',', quotechar='"')
for row in csv_reader:
    print(row)
input_file.close()
