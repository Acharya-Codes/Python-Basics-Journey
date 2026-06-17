class Student:
    count = 0
    total_gpa = 0

    def __init__(self,student,gpa):
        self.student = student
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #Instance Method:
    def get_info(self):
        return (f"{self.student} = {self.gpa}")

    #Class Method:
    @classmethod
    def get_count(cls):  # Bascially like self for instance and static method...there exists cls for class method!
        return (f"Total number of student: {cls.count}")
    @classmethod
    def get_avg_gpa(cls):
        if cls.total_gpa == 0:
            return 0
        else:
            print(f"{cls.total_gpa/cls.count:.3f} is the average gpa")

student1 = Student("Acharya",8)
student2 = Student("Siddhesh",7.5)

print(Student.get_count())
Student.get_avg_gpa()