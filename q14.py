questions = ((" What is the capital of France?: "),
("Which planet is known as the Red Planet?: "),
("Who wrote the Indian national anthem?: "),
("What is the largest ocean in the world?: "),
("How many players are there in a cricket team on the field?: "))

options=((("A)Madrid"),("B)Berlin"),("C)Paris"),("D)Rome")),
(("A)Earth"),("B)Mars"),("C)Venus"),("D)Jupiter")),
(("A)Gandhiji"),("B)Rabindranath Tagore"),("C)Netaji"),("D)Indhra Gandhi")),
(("A)Pacific Ocean"),("B)Atlantic Ocean"),("C)Artic Ocean"),("D)Indian Ocean")),
(("A)10"),("B)11"),("C)12"),("D)9")))

answers=(("C"),("B"),("B"),("A"),("B"))
guesses=[]
question_num=0
score=0


for question in questions:
    print("------------")
    print(question)
    for option in options[question_num]:
        print(option)
    

    inp = input("Enter (A,B,C,D): ").upper()
    guesses.append(inp)
    if inp == answers[question_num]:
        score +=  1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("--------#------#-----")
if score == 5:
    print("You da real topper!")
    print(f"Your total score is: {score}/5")
elif score < 5 and score >2:
    print("Meh")
    print(f"Your total score is: {score}/5")
else:
    print("TRASH")
    print(f"Your total score is: {score}/5")


            
       