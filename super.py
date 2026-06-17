class Shape:
    def __init__(self,colour,filled):
        self.colour = colour
        self.filled = filled
    def describe():
        print(f"It is {self.colour} and {"Filled" if self.filled else "Not filled"}")
class Circle(Shape):
    def __init__(self,colour,filled,radius):
        super().__init__(colour,filled)   #Or we can use this line too.... Shape().__init__(self,colour,filled,radius)
        self.radius=radius
class Square(Shape):
    def __init__(self,colour,filled,sides):
        super().__init__(colour,filled)
        self.sides = sides

circle = Circle("Red","Yes",5)
square = Square("Blue","No",6)

print(circle.colour)
print(square.sides)
circle.describe()
square.describe()   # We can override the describe function too