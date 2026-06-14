word  = "APPLE"
game=input("Guess a letter in the word: ").upper()
if game in word :
    print("Your guess is correct!")
else:
    print("Wrong guess!")