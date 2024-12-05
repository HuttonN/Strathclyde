from datetime import datetime
import csv


class File:
    """
    A class to represent a file, including a name
    size, executable, content and modification datetime string.
    """
    def __init__(self,
                 name,
                 size,
                 executable=False,
                 content="",
                 modified=""):
        self.name = name
        self.size = size
        self.executable = executable
        self.content = content
        if len(modified) == 0:
            self.modified = datetime.now()
        else:
            self.modified = datetime.fromisoformat(modified)

    def __repr__(self):
        s = "File("
        s += f"name='{self.name}',"
        s += f"size={self.size},"
        s += f"executable={self.executable},"
        s += f"content='{self.content}',"
        s += f"modified='{self.modified.isoformat()}')"
        return s

    def __eq__(self, other):
        return ((self.name == other.name) and
                (self.size == other.size) and
                (self.executable == other.executable) and
                (self.content == other.content) and
                (self.modified == other.modified))


class Directory:
    """
    A class to represent a directory of zero or more
    files.
    """
    def __init__(self,
                 name,
                 files=[]):
        self.name = name
        self.files = files.copy()

    def __repr__(self):
        s = "Directory("
        s += f"name='{self.name}',"
        s += f"files={self.files}"
        s += ")"
        return s

    def total_size(self):
        """
        A function to return the total size of all files
        within this directory.
        """
        total = 0
        for file in self.files:
            total += file.size
        return total

    def to_csv(self, file_name):
        """
        A function to write File objects from a CSV file.
        """
        output_file = open(file_name, "w", encoding="utf-8", newline="")
        fieldnames = [
            "name",
            "size",
            "executable",
            "content",
            "modified"
        ]
        dict_writer = csv.DictWriter(output_file,
                                     fieldnames,
                                     quoting=csv.QUOTE_NONNUMERIC)
        dict_writer.writeheader()
        for file in self.files:
            row_dict = {
                "name": file.name,
                "size": file.size,
                "executable": str(file.executable),
                "content": file.content,
                "modified": file.modified.isoformat()
            }
            dict_writer.writerow(row_dict)
        output_file.close()

    def from_csv(self, file_name):
        """
        A function to read File objects from a CSV file.
        """
        self.files.clear()
        input_file = open(file_name, "r", encoding="utf-8", newline="")
        dict_reader = csv.DictReader(input_file,
                                     quoting=csv.QUOTE_NONNUMERIC)
        for dict_row in dict_reader:
            file = File(
                dict_row["name"],
                dict_row["size"],
                dict_row["executable"].lower() == "true",
                dict_row["content"],
                dict_row["modified"]
            )
            self.files.append(file)
        input_file.close()
