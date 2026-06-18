import csv
file_path = "output3.csv"
try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for item in content:
            print(item) # We can use indexing here too
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission not granted to read this file")