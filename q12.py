#Shopping cart for foods with prices
foods=[]
prices=[]
total=0

while True:
    food = input("Enter the food u would like to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the prices of the food u bought {food} : "))
        foods.append(food)
        prices.append(price)
        total += price
        
    
print("-----MY SHOPPING CART-----")
for food in foods:
    print(food,end=" ")
    print(price,end=" ")