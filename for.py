#This loop can be used to run a block of code a fixed number of timez!
for x in range(1,11):
    print(x)
for y in reversed(range(1,11)): #Basically reversal of the same output as x!
    print(y)
for z in range(1,11,2): #Same like indexing
    print(z)

for a in range(1,21):
    if a==13:
        continue    #To skip over an iteration we can use the continue keyword!
    else:
        print(a)
           
for b in range(1,11):
    if b==6:
        break  #To break the loop after a certain output is reached in the loop!
    else:
        print(b)
