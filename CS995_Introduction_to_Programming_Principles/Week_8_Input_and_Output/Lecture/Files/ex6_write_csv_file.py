import csv


"""
A program to write a CSV file with the CSV
writer.
"""
output_file = open("my-file.csv", "w", newline='')
csv_writer = csv.writer(output_file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_NONNUMERIC)
csv_writer.writerow(["Host", "IP"])
csv_writer.writerow(["localhost", "127.0.0.1"])
output_file.close()
