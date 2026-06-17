class Student:
    year = 2024
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1 = Student("Spongebob",30)
student2 = Student("Patrick",35)

print(student1.name)
print(student2.age)
print(Student.year)
print(Student.year)