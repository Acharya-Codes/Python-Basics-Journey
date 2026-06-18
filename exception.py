try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can divide by zero bruh")
except ValueError:
    print("This is not a number bruh")
except Exception: # Usually telling the users what is the error is better so dont use this much!
    print("Something went wrong")
finally: #It always runs regradless if there is an exception or not!
    print("Do some cleanup here")