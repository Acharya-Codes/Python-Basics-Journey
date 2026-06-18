# A function which extends the behavior of another function without modifying base function!
def add_sprinkles(func):
    def wrapper(*args,**kwargs):   # This wrapper function makes sure that the statements will be executed only when called!
        print("Added some sprinklers")
        func(*args,**kwargs)
    return wrapper
def add_fudge(func):
    def wrap(*args,**kwargs):
        print("Added some fudge")
        func(*args,**kwargs)
    return wrap

@add_sprinkles  #We can apply more than 1 decorator to the base function!
@add_fudge
def get_ice(flavour):
    print(f"Here is your {flavour} icecream 🍧")

get_ice("chocolate")