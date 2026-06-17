import random

words = ("apple","orange","banana","watermelon")

hangman = {0:("   "
              "   "
              "   "),


           1:(" o "
              "   "
              "   "),


           2:("  o "
              "  | "
              "    " ),

           3:("   o  "
              "  /|  "
              "      "),


           4:("  o   "
              " /|\\ "
              "      "),

           
           5:(" o    "
              "/|\\  "
              "/ \\  "),

           6:("📿💀")}

def disp(wrong):
    for line in hangman[wrong]:
        print(line)

def hints(hint):
    print(" ".join(hint))
def answer(ans):
    print(ans)
def main():
    ans=random.choice(words)
    hint=["_"] * len(ans)
    wrong=0
    guessed_letter=set()
    is_running=True
    while is_running:
        disp(wrong)
        hints(hint)
        guess = input("Enter your guess: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only one character")
            continue  # Keyword to skip the loop
        if guess in guessed_letters:
            print(f"{guess} is aready guessed")
            continue
        guessed_letters.add(guess)
        
        if guess in ans:
            for index in range(len(answer)):
                if ans[i] == guess:
                    hint[i] = guess
        else:
            wrong += 1

        if "_" not in hint:
            disp(wrong)
            answer(ans)
            print("You win!")
            is_running=False
        elif wrong >= len(hangman)-1:
            disp(wrong)
            answer(ans)
            print("You lose!")
            is_running=False



if __name__ == "__main__":
    main()


    
