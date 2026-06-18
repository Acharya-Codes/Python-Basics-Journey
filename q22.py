import random
def spin():
    symbols = ["🤑","😘","😁"]
    return [random.choice(symbols) for _ in range(3)]
def printt(row):
    print("--------")
    print(" | ".join(row))
    print("--------")
def gveamt(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🤑":
            return bet*5
        elif row[0] == "😘":
            return bet*4
        elif row[1] == "😁":
            return bet*3
    else:
        print("Sorry broh u lost")
        return 0
        
              
                  
           
def main():
    balance = int(input("Please enter the amount u wanna store to gamble: "))    
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("-----Welcome to Aachi's gambling-----")
        print("Symbols: 🤑 😘 😁")
        
        while balance > 0:
            
            print(f"Current balance is: {balance}")
            bet = int(input("Enter the bet amount u wanna place: "))
            if bet <= balance:
                print("You can proceed...Enojy the game😈")
                balance -= bet
                print(f"NOTE: Your current balance is: {balance}")
                row = spin()
                print("Ur fate is being decided broh.....\n")
                printt(row)
                win = gveamt(row,bet)
                print(win)
                if win > 0:
                    print("You hit the JACKPOT!!")
                    print(f"Your balance has been updated: {win}")
                balance += win
                    
                

            else:
                print("You broke homie u cant proceed😂")


    else:
        print("Sorry lil bro u can't gamble😂!")
        print("Your money has been refunded dont worry😉")

if __name__ == "__main__":
    main()



