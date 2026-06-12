name = input("Enter a valid username: ")
length = len(name)
antidigits = name.isalpha()
spaces = name.find("")

print("Valid username" if length < 12 and antidigits and  spaces==-1 else "Enter a valid username")