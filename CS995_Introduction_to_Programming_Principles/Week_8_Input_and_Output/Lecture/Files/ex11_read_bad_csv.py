import csv


def seek_comma(text_io):
    """
    A function to advance the file position to the
    first line that contains a comma.  The function
    returns False if the end-of-file is reached.
    """
    # Advance to the first line that contains a comma.
    while True:
        # Get the current position of the file cursor.
        position = text_io.tell()

        # Read one line.
        line_text = text_io.readline()

        # Check if the end of file has been reached.
        if len(line_text) == 0:
            return False

        # Check if the line contains a comma.
        if "," in line_text:
            # Rewind to start of line.
            text_io.seek(position)
            return True


"""
A program to demonstrate using the file cursor
to avoid reading the inital section of a file.
"""
input_file = open("bad_file.csv", "r", newline='')
if seek_comma(input_file):
    csv_reader = csv.reader(input_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        print(row)
input_file.close()
