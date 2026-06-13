menu = {"dosa":20,"idli":20,"chapathi":30,"semiya":40}
waiter=[]
total=0

print("-------Hotel Achi-------")
for key,value in menu.items():
    print(f"{key} --> {value}")
    
print("-------Enjoy the food :)-------")

while True:
    food = input("Enter the dishes u wanna buy (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        waiter.append(food)

for food in waiter:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"Your total is: {total}")
print("Thank you for coming hope we will see you soon again!")