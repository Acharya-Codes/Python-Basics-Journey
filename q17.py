import random
is_running=True
options=["Rock","Paper","Scicor"]
game = random.choice(options)

print("--Welcome to the nostalagic Rock Paper Scicor game!--")
while is_running:
    game = random.choice(options)
    wish = input("Choose your weapon!(Rock/Paper/Scicor): ")
    if game == "Rock":
        if wish == "Rock":
            print("Neutralised")
            print(f"System's choice: {game}")
            print("Try again")
            
        elif wish == "Scisor":
            print("You trash broh u lost!")
            print(f"System's choice: {game}")
            print("Try again")
            is_running=False
        else:
            print("You won!!")
            print(f"System's choice: {game}")
            print("---Hope you liked it!---")
            is_running=False
    elif game == "Paper":
        if wish == "Rock":
            print("You trash broh u lost!")
            print(f"System's choice: {game}")
            print("Try again")
            is_running=False
        elif wish == "Paper":
            print("Neutralised")
            print(f"System's choice: {game}")
            print("Try again")
            
        else:
            print("You won!!")
            print(f"System's choice: {game}")
            print("---Hope you liked it!---")
            is_running=False
    else:
        if wish == "Paper":
            print("You trash broh u lost!")
            print(f"System's choice: {game}")
            print("Try again")
            is_running=False
        elif wish == "Scisor":
            print("Neutralised")
            print(f"System's choice: {game}")
            print("Try again")
            
        else:
            print("You won!!")
            print(f"System's choice: {game}")
            print("---Hope you liked it!---")
            is_running=False

