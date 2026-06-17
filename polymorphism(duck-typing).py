# Analogy : If it looks like a duck and quacks like a duck , then must be a duck!

class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("Wooff!")
class Cat(Animal):
    def speak(self):
        print("Meoww!")
class Car:
    def speak(self):   # 2.But when we change the horn(self) to speak(self) it meets the minimum requirement  so it will print clearly!
        print("Honkk!")

animals = [Dog(),Cat()]
for animal in animals:
    animal.speak()
    print(animal.alive)

# 1.If we get the output then we will get an attribute error for the Car class as it is not related to the Animal class

# Now the alive method will show who is the imposter as the class Car is not realted with Animal class so it will show false while Dog and Cat class will show true!!