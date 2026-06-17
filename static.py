class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def get_info(self):   # Instance Method!
        return (f"{self.name} = {self.position}")

    @staticmethod   # Static Method!
    def is_valid_position(position):
        valid_positions = ["Manager","Casheir","Cook","Janitor"]
        return position in valid_positions

employee1 = Employee("Acharya","Manager")
employee2 = Employee("Kavi","Cashier")
employee3 = Employee("Siddhesh","Cook")
employee4 = Employee("Karun","Janitor")

a = input("Enter your position in the company: ")
print(Employee.is_valid_position(a))

#Instance Method : You have to call the object and use the method (Object is MUST to create to use this method)!
#Staic Method : We can use the method without objects from the class (General Utility Method)!