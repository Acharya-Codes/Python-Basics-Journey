def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")
hello("Hi","Mr","Acharya","N") # RN we are using positional arguements as if we change their positions output will vary!

hello("Hi",last="N",first="Acharya",title="Mr") # This is keyword arguements where the position doesnt matter!!

#Positional arguements follow keyword arguements!!