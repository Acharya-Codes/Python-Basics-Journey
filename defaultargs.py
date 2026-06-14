import time
def count(end,start=0): #start=0 is a default arguement as we set one of the parameters fixed
    for x in range(start,end+1): #end is a positional arguement as it is variable
        print(x)
        time.sleep(1)
    print("The End")
count(10)
