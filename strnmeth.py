#Some string methods

#Length (Calculates the length of the string including spaces)
name = input("Enter your full name: ")
result = len(name)
print(result)

# (.) methods for string

#Find (Finds the position of the first occurance of a letter/space in the given string) (Begins from 0)
namee = "Acharya"
resultt = namee.find("c")
#If there is no letter matching the given letter the program will return "-1"

#rfind (Same as find but in reverse)

#capitalize (Makes the first letter of the string into capital)
#upper (Makes the entire string caps)
#lower (Makes the entire string lower case)