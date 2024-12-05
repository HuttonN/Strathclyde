from datetime import datetime
import csv
import re

class File:
    def __init__(self, name: str, size: int, executable: bool = False, content: str = "", modified: str = ""):
        self.name = name
        self.size = size
        self.executable = executable
        self.content = content
        self.modified = datetime.fromisoformat(modified) if modified else datetime.now()

    def __repr__(self):
        return (f"File(name=\"{self.name}\", size={self.size}, executable={self.executable}, "
                f"content=\"{self.content}\", modified=\"{self.modified.isoformat()}\")")

    def __eq__(self, other):
        if isinstance(other, File):
            return (self.name == other.name and self.size == other.size and 
                    self.executable == other.executable and self.content == other.content and
                    self.modified == other.modified)
        return False

class Directory:
    def __init__(self, name: str, files: list = None):
        self.name = name
        self.files = files[:] if files else []
    
    def __repr__(self):
        return f"Directory(name=\"{self.name}\", files={self.files})"
    
    def total_size(self):
        return sum(file.size for file in self.files)
    
    def to_csv(self, output_filename: str):
        with open(output_filename, "w", newline='', encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["name", "size", "executable", "content", "modified"])
            for file in self.files:
                writer.writerow([file.name, file.size, file.executable, file.content, file.modified.isoformat()])

    def from_csv(self, input_filename: str):
        with open(input_filename, "r", newline='', encoding="utf-8") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                self.files.append(File(
                    name=row["name"],
                    size=int(row["size"]),
                    executable=row["executable"].lower() == "true",
                    content=row["content"],
                    modified=row["modified"]
                ))

    def find_by_name(self, search_string: str):
        try:
            match_alg = re.compile(search_string)
            return [file for file in self.files if match_alg.match(file.name)]
        except re.error:
            return []

    def find_by_modified(self, modified: datetime, comparison: int = 0):
        if comparison == 0:
            return [file for file in self.files if file.modified <= modified]
        elif comparison == 1:
            return [file for file in self.files if file.modified >= modified]
        return []
