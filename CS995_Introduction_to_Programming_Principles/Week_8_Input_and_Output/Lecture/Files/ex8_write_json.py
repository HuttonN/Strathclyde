import json


"""
A program to write a JSON file.
"""
hosts = {}
hosts["localhost"] = "127.0.0.1"
output_file = open("my-file.json", "w", encoding="utf-8")
json.dump(hosts, output_file, ensure_ascii=False, indent=4)
output_file.close()
