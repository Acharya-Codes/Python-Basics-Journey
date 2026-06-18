import csv
employees = [["Name","Age","Job"],
             ["Acharya",17,"Manager"],
             ["Kavi",17,"Cashier"],
             ["Siddhesh",17,"Janitor"]]
file_path = "output3.txt"
try:
    with open(file_path,"w",newline="") as file3:  #This newline keyword can be used to prevent spaces between rows!
        writer = csv.writer(file3)
        for row in employees:
            writer.writerow(row)
        print(f"{file_path} has been created succesfuly in csv type")
except FileExistsError:
    print("That file already exists")