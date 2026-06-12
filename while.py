name = input("Enter your name: ")
while name == "":
    print("The name cannot be empty")
    name = input("Enter your name: ")
print(f"Hello {name}")

#Uptil some condition we entered is true the while loop will keep on lopping infinitley!!