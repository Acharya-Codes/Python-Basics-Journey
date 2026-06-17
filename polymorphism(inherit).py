from abc import ABC , abstractmethod
class Shape(ABC):  # We have to connect the ABC(abstract method) class to the shapes method for the abstract method to work
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,sides):
        self.sides = sides
    def area(self):
        return self.sides ** 2

a = int(input("Enter the radius to find the area of the circle: "))
b = int(input("Enter the side length of the square to find the area of the square: "))
shapes = [Circle(a),Square(b)]

for shape in shapes:
    print(f"{shape.area()}cm^2 is the area!")