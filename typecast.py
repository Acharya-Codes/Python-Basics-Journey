#TypeCasting basically means conversion of one datatype into another!
name = "Acharya"
age = 17
percentage = 84.1
is_student = False

percentage = int(percentage) #This will convert the percentage from float to int!
print(percentage)
age = float(age) #Vice versa of the int() function!
print(age)
age = str(age) #Int to string!
print(age)
percentage = str(percentage) #Float to str!
print(percentage)
#bool() doesnt make sense without the scanner variable as it will always return true!