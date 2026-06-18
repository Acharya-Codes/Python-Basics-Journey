import json
file_path = "output2.json"
try:
    with open(file_path,"r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission not granted to read this file")