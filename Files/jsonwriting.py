import json
employees = {"Name":"Acharya","Age":30,"Role":"Manager"}
file_path = "output2.json"
try:
    with open(file_path,"w") as file2:
        json.dump(employees,file2)  # This method allows us to conver the dict to json string line
        for employee in employees:
            print(f"{file_path} has been created as a json file")
except FileExistsError:
    print("That file already exists")

