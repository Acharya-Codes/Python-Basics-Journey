#Compound Intrest Calculator

# A = P(1+[R/N])^T

#A --> Final amount
#P --> Initial principal amount
#R --> Annual Intrest Rate
#N --> No of times compounded per year!
#T --> Time in years

p=float(input("Enter a principle amount: "))

while p <= 0:
    print("Principle amount cant be zero or negative")
    p=float(input("Enter a principle amount: "))

r=float(input("Enter the annual intrest rate: "))/100
while r <= 0:
    print("The annual intrest rate cannot be zero or negative")
    r=float(input("Enter the annual intrest rate: "))/100

t=float(input("Enter the total time period (in yrs): "))
while t <= 0:
    print("The time period cannot be zero or negative")
    t=float(input("Enter the total time period (in yrs): "))

n=int(input("Enter the number of times the amount has been compounded per year: "))
while n <= 0:
    print("The number cannot be zero or negative")
    n=int(input("Enter the number of times the amount has been compounded per year: "))

a = p*pow((1+(r/n)),n*t)
print(f"Your final amount is: {a:,}")