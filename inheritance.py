class Animal:
    def __init__(self,name):
        self.name=name
    def eat():
        print("The animal is eating")
    def sleep():
        print("The animal is sleeping")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog("Jimmy")
cat = Cat("Billy")
print(dog.name)
print(cat.sleep)
