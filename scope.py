def func1():
    x=1    # This x is local to func1
    print(x)
def func2():
    x=2    # This x is local to func2
    print(x)
func1()  #Output is 1
func2()   #Output is 2

#But what if func2 was inside(enclosed) of func1?

def func1():
    y=1
    def func2():
        y=2
        print(y)
    func2()
func1()
# For this the output is 2 and not 1
# This is where scope resolution comes in
# It follows an order of LEGB --> Local Enclosed Global Built-In

# So here the enclosed one is given more pref acc. to the LEGB rule of scopes!!!
# Local gets the most priority
# Then comes Enclosed
# Then comes Gloabal
# Then comes Built-In

def func1():
    print(z)
def func2():
    print(z)
z=3
func1()
func2()  
# Both of the outputs will be 3 as there is no local or enclosed version of z so it moves to the global 

from math import e

def func1():
    print(e)
e=3
func1()
# Here the output will be 3 as per the LEGB rule!!!