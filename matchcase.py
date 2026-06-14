# An alternate to using many elif statements!!
def day_of_week(day):
    match day:
        case 1:
            print("It is Sunday")
        case 2:
            print("It is Monday")
        case 3:
            print("It is Tuesday")
        case 4:
            print("It is Wednesday")
        case 5:
            print("It is Thursday")
        case 6:
            print("It is Friday")
        case 7:
            print("It is Saturday")
        case _:
            print("Not a valid day")

day_of_week(1)

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Satruday":
            return True
        case _:
            return False

print(is_weekend("Monday"))

#This can be even more simplified using the or | operator!!

def is_weekend(day):
    match day:
        case "Saturday"|"Sunday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))