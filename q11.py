rows = int(input("Enter the number of rows u want: "))
column = int(input("Enter the number of columns u want: "))
symbol = input("Enter the symbol u want to use: ")

for x in range(rows):
    for y in range(column):
        if x == 0 or x == rows-1 or y == 0 or y == column-1:
            print(symbol,end="")
        else:
            print(" ",end="")
    print()       

    