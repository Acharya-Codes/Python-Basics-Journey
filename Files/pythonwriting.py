employees = ["Acharya","Kavi","Siddhesh"]
file_path = "output.txt"
with open(file_path,"w") as file2: # w for write , x also to write but used when the text file doesnt exist!
    for employee in employees:
        file2.write(employee + "\n")
        print(f"{file_path} as a text file was created")