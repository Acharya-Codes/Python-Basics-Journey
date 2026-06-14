doubles=[x*2 for x in range(1,11)]
print(doubles) # Consice wat to create lists in python!

numbers = [1,4,5,-3,-2,-1]
num = [num for num in numbers if num > 0]
print(num)

grades=[85,69,42,99,10]
gr = [gr for gr in grades if gr > 60]
print(f"Congrats broh u passed!{gr}")