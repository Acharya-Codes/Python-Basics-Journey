#Temperature Converter
temp = float(input("Enter the temperature: "))
conv = input("Is this temp in Celsius or Faranheit? (C/F): ")

if conv == "F":
    temp = (9*temp +160)/5
    unit = "C"
    print(f"The temperature is {temp} {unit}")
elif conv == "C":
    temp=(temp-32)*5/9
    unit = "F"
    print(f"The temperatur is: {temp} {unit}")
else:
    print("Not valid input")