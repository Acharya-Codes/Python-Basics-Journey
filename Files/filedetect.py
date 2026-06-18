import os
file_path = "file1.txt"  #Relative path
if os.path.exists(file_path):
    print(f"{file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):  #To detect if the file is in a directory(dir) or not!
        print("That is a directory")
else:
    print(f"{file_path} doesn't exists")

#Let's say we create a new directory of python and move the file.txt into it
#Then the rleative path wont work so we have to type
# file_path = "stuff/file1.txt" (stuff being the name of the directory)