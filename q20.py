def label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for keys,values in kwargs.items():
        print(f"{keys}:{values}",end=" ")
    print()

name=label("Mr","Acharya","N",city="Texas",street="Fakey",apt=69,zip=12345)
