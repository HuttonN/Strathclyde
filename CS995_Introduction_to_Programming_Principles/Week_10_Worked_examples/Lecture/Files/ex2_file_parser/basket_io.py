from datetime import datetime

__start_record__ = "BEGIN RECORD"
__end_record__ = "END RECORD"


class BasketItem:
    """
    A class to represent an item within a shopping basket.
    """
    def __init__(self,
                 name="",
                 quantity=0,
                 modified=""):
        self.name = name
        self.quantity = quantity
        if len(modified) == 0:
            self.modified = datetime.now()
        else:
            self.modified = datetime.fromisoformat(modified)

    def __repr__(self):
        s = "BasketItem("
        s += f"name=\"{self.name}\","
        s += f"quantity={self.quantity},"
        s += f"modified=\"{self.modified}\""
        s += ")"
        return s


def list_to_file(text_io, records):
    """
    A function to write one or more objects to a record
    within a text file.  The function relies on __repr__
    for serialisation of the objects.
    """
    for record in records:
        text_io.write(f"{__start_record__}\n")
        for obj in record:
            text_io.write(f"{obj}\n")
        text_io.write(f"{__end_record__}\n")


def file_to_list(text_io, records):
    """
    A function to read one or more objects from text
    file records.  The objects are assumed to be written
    as strings that can be evaluated to create the objects.
    """
    records.clear()
    in_record = False
    while True:
        line = text_io.readline()
        if len(line) == 0:
            break
        line = line.strip()
        if line == f"{__start_record__}":
            in_record = True
            objs = []
            continue
        if line == f"{__end_record__}":
            in_record = False
            records.append(objs)
            objs = []
            continue
        if in_record:
            objs.append(eval(line))


def main():
    """
    A program to write and read objects
    from a text file.
    """
    time_now = datetime.now()
    time_str = time_now.isoformat()
    records = [
        [
            BasketItem("Apple", 2, time_str),
            BasketItem("Pear", 3, time_str)
        ],
        [
            BasketItem("Apple", 10, time_str),
            BasketItem("Orange", 5, time_str)
        ]
    ]

    # Write the records.
    output_file = open("basket.txt", "w")
    list_to_file(output_file, records)
    output_file.close()

    # Read the records.
    input_file = open("basket.txt")
    read_records = []
    file_to_list(input_file, read_records)
    print(read_records)


if __name__ == "__main__":
    main()
