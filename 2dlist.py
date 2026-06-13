fruits = ["apple","orange","banana"]
vegetables = ["carrot","beetroot","tomato"]
meats = ["chicken","pork","fish"]

groceries = [fruits,vegetables,meats]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()