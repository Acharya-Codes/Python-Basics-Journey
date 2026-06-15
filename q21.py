balance=0

is_running=True

def show_balance():
    print(f"Your balance is: {balance}")
    
def deposit():
    
    global is_running
    global balance # As balance is a global variable we have to use the gloabal keyword
    dep = int(input("Enter the non negative amount u wanna deposit: "))
    balance += dep  
    ch1 = input("Do you want to check ur balance?(Yes/No): ").capitalize()
    if ch1 == "Yes":
        print(f"Your balance is: {balance}")
    else:
        is_running=False
        print("---Thank you for visiting us!---")

def withdraw():
    
    global is_running
    global balance # As balance is a global variable we have to use the gloabal keyword
    wit = int(input("Enter the non negative amount u wanna withdraw: "))
    balance -= wit  
    wit1 = input("Do you want to check ur balance?(Yes/No): ").capitalize()
    if wit1 == "Yes":
        print(f"Your balance is: {balance}")
    else:
        is_running=False
        print("---Thank you for visiting us!---")


while is_running:
    print("Welcome to Aachi's Bank")
    print("1.Register a new account")
    print("2.Login")
    req = int(input("Select your action(1 or 2): "))
    
    if req == 1:
        
        a = int(input("Enter a non negative amount to add to your balance: "))
        balance = a
        print(f"Your balance has been updated to: {a}")
    else:
        print("Welcome to Aachi's Bank")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Choose your action (1 to 4): ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            is_running=False
            print("---Thank you for visiting us!---")
        else:
            print("That is not a valid choice")


    
        
