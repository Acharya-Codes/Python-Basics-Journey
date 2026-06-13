import random

dice=random.randint(1,6) #This randint() function will generate a random number between the given range!
print(dice)

options1 = ("rock","paper","scissors")
game1 = random.choice(options1)
print(game1)

options2 = [2,3,4,5,6,7,8,9,10,"J","K","Q","A"]
random.shuffle(options2)
print(options2)