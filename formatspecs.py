# Format Specifiers = {value:flags} --> These flags will format a value!

price1 = 300.1415
price2 = -954.84
price3 = 1224.36

print(f"The price is: {price1:.3f}") # (.nf) where n is a positive integer will help to specify how many decimals need!

print(f"The price is: {price2:10}") # (n) will leave n amount of gaps!

print(f"The price is: {price3:010}") # (0n) will fill the gaps with zeroes!

print(f"The price is: {price1:<10}") # (<) Left aligned for 10 speaces!

print(f"The price is: {price2:>10}") # (>) Right aligned for 10 speaces!

print(f"The price is: {price3:^10}") # (^) Center aligned for 10 speaces!

print(f"The price is: {price1:,}") # (,) It will insert commas according to the number system!

#Flags can be combined too!!!