import json


"""
A program to read a JSON file and print it.
"""
input_file = open("my-file.json", "r", encoding="utf-8")
json_data = json.load(input_file)
input_file.close()
print(json_data)
