#Basic Calculator
a = float(input("Enter the first variable: "))
b = float(input("Enter the second variable (Non zero): "))
q = input("What kind of operation would u like to do?(Add/Sub/Mul/Div): ")

if q == "Add":
    print(a+b)
elif q == "Sub":
    x=abs(a-b)
    print(x)
elif q == "Mul":
    print(a*b)
elif q == "Div": 
    print(a/b)
else:
    print("Invalid Operation")

#Learning step by step so error handelling didnt use in this one 