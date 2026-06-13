import random
lowest = 1
highest = 100
ans=random.randint(lowest,highest)
guesses=0
is_running=True

print("------Python number guess game!------")

while is_running:
    g = input("Guess a number between 1 and 100: ")
    if g.isdigit():
        g=int(g) # As the input function gives us the input in terms of string
        guesses += 1

        if g < 1 or g > 100:
            print("Invalid Guess")
            print("Please guess a number between 1 and 100")
        elif g < ans:
            print("Too low bruh")
        elif g > ans:
            print("Too high bruh")
        else:
            print("Congrats homie u won the game")
            print(f"You took {guesses} amount of guesses")
            print("---Hope u likes this---")
            is_running=False
                

    else:
        print("Invalid Guess")
        print("Please guess a number between 1 and 100")
