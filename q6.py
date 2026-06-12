#Weight Converter
weight = float(input("Enter your weight: "))
unit = input("Kg or pounds?: ")
if unit == "kg":
    weight = weight * 2.205
    unit="pounds"
elif unit == "pounds":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"The unit was not valid")
    exit()
print(f"Your weight is: {round(weight,2)} {unit}")