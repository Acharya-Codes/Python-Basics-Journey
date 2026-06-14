def add(*args): 
    total=0    # *args = Allows us to use multiple no key arguments 
    for arg in args:   # We can use any name not only args after the *
        total += arg
    return total
print(add(1,2,3,4,5,6))

def name(*kwargs):
    for kwarg in kwargs: #kwargs = Allows us to use multiple key arguements  and we can change the name similar to args
        tot_name=kwarg
    return tot_name
print("Acharya","N")