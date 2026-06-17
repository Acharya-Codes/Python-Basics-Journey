class Eat:
    def eat(self):
        print("The animal is eating")
class Sleep:
    def sleep(self):
        print("The animal is sleeping")
class Dog(Eat,Sleep):
    pass

dog=Dog()
print(dog.eat)
print(dog.sleep)

