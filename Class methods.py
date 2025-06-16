class Student:

    count = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    #INSTANCE METHOD
    def get_info(self):
            return f"{self.name} {self.gpa}"
        
    @classmethod
    def get_count(cls):
            return f"Total no of students: {cls.count}"
        
student1 = Student("Alice",4.2)
student2 = Student("Geminer",3.0)
student3 = Student("vaden",4.0)

print(Student.get_count())


