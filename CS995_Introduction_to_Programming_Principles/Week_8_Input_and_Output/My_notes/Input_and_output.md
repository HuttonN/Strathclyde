# Input and Output in Python

## Introduction

* **Scope:** Focus on basic input and output (I/O) operations; not covering complex formats like Excel or databases in this module.
* **Types of File Formats:**
    * **Text Files:** Readable by text editors, e.g., Notepad.
    * **Binary Files:** Encoded data; unreadable by text editors.
* **Beyond Files:**
    * Databases (e.g., SQLite, relational databases with SQL, NoSQL like MongoDB).
    * Devices (e.g., sensors, motor drivers).
    * Network communications (e.g., sending/receiving data over Wi-Fi).

## File Operations Overview

### Working with File Paths

* Use absolute paths (start from root, e.g., ```C:\users\file.txt```) or relative paths (relative to current working directory).
* To ensure compatibility across operating systems, use ```os.path.join()```:

Example:

```python
import os.path

file_path = os.path.join("my_dir", "my-file.txt")
print(f"file_path=\"{file_path}\"")
```

### Checking File or Directory Existence

* Use ```os.path.isfile()``` to check if a file exists and ```os.path.isdir()``` for directories.

Example:

```python
import os.path

file_name = "my-file.txt"
exists = os.path.isfile("my-file.txt")
if exists:
    print(f"The file \"{file_name}\" exists.")
else:
    print(f"The file \"{file_name}\" does not exist.")
```

### Getting File Size

* Retrieve the size of a file using ```os.path.getsize()```:

Example:

```python
import os.path

file_name = "my-file.json"
file_size = os.path.getsize(file_name)
print(f"{file_name} is {file_size} bytes.")
```

## Writing and Reading Text Files

### Writing Text Files

1. Open a file in write mode: ```open('file.txt', 'w')```.
1. Write to the file: ```file.write("Content\n")```.
1. Close the file: ```file.close()```.
 
Example:

```python
output_file = open("written-file.txt", "w")
output_file.write("A text string" + "\n")
output_file.close()
```

### Reading Text Files

1. Open a file in read mode: ```open('file.txt', 'r')```.
1. Read the content:
    * Entire file: ```file.read()```.
    * Line-by-line: ```file.readline()``` or ```file.readlines()```.
1. Strip whitespace: ```.strip()```.
1. Close the file: ```file.close()```.

Example:

```python
input_file = open("written-file.txt", "r")
content = input_file.read()  # Read all lines of the file.
content = content.strip()    # Remove trailing new line.
print(content)
input_file.close()
```

## Working with CSV Files

### Writing CSV Files

1. Open a file in write mode: ```open('file.csv', 'w', newline='')```.
1. Create a CSV writer object: ```csv.writer(file, delimiter=',')```.
1. Write rows:
    * Header: ```writer.writerow(['Column1', 'Column2'])```.
    * Data rows: ```writer.writerow([value1, value2])```.
1. Close the file: ```file.close()```.
1. 
Example:

```python
import csv

output_file = open("my-file.csv", "w", newline='')
csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
csv_writer.writerow(["Host", "IP"])
csv_writer.writerow(["localhost", "127.0.0.1"])
output_file.close()
```

### Reading CSV Files

1. Open a file in read mode: ```open('file.csv', 'r', newline='')```.
1. Create a CSV reader object: ```csv.reader(file, delimiter=',')```.
1. Iterate through rows: for ```row``` in ```reader```: ```print(row)```.
1. Close the file: ```file.close()```.
1. 
Example:

```python
import csv

input_file = open("my-file.csv", "r", newline='')
csv_reader = csv.reader(input_file, delimiter=',', quotechar='"')
for row in csv_reader:
    print(row)
input_file.close()
```

### Using ```DictReader``` for CSV

* Read CSV rows into dictionaries, using the first row as column headers.

Example:

```python
import csv

input_file = open("test.csv")
dict_reader = csv.DictReader(input_file)
for row in dict_reader:
    print(row)
input_file.close()
```

## Working with JSON Files

### Writing JSON Files

1. Create a dictionary or list: ```data = {"key": "value"}```.
1. Open file in write mode: ```open('file.json', 'w', encoding='utf-8')```.
1. Write using ```json.dump(data, file, indent=4)```.
1. Close the file: ```file.close()```.

Example:

```python
import json

hosts = {}
hosts["localhost"] = "127.0.0.1"
output_file = open("my-file.json", "w", encoding="utf-8")
json.dump(hosts, output_file, ensure_ascii=False, indent=4)
output_file.close()
```

### Reading JSON Files

1. Open file in read mode: ```open('file.json', 'r', encoding='utf-8')```.
1. Load content: ```data = json.load(file)```.
1. Close the file: ```file.close()```.

Example:

```python
import json

input_file = open("my-file.json", "r", encoding="utf-8")
json_data = json.load(input_file)
input_file.close()
print(json_data)
```

## Error Handling and Best Practices

### File Cursors

* Files are read line-by-line; the cursor tracks the current position.
* Reposition cursor using ```.seek()```.

### Validation

* Always check file existence before reading.
* Close file connections to free resources.

### Use of ```with```

* Automates file closing after operations:
```python
with open("file.txt", "r") as file:
    content = file.read()
```

### Dealing with Malformed Files

* Pre-read lines to identify valid content.
* Skip invalid lines using custom functions.

## Summary

* **I/O Basics:** Essential for handling text, CSV, and JSON files.
* **Modularity:** Integrate I/O operations into reusable functions.
* **Error Handling:** Close files, validate inputs, and handle edge cases like malformed files.
* **Further Exploration:** More advanced topics like databases and network I/O will be covered in future modules.