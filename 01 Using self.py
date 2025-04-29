# 06- Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series:
By Moiz Iqbal

1- Using Self

Create a class Student with attributes name and marks. Use the self keyword to
initialize these values via a constructor. Add a method display() that prints
student details. #


class Student:    
    #  initialize name and marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # display student details
    def display(self):
        print(f"student name is : {self.name}")
        print(f"student marks is : {self.marks}")
student1 = Student("Moiz",87)
student1.display()

#second step

class Student2:
    def __init__(self,tuesday,wednesday,thursday):
        self.thursday = thursday
        self.wednesday = wednesday
        self.tuesday = tuesday
    def display(self):
            print(f"yur subjects on tuesday is : {self.tuesday}")
            print(f"your subjects on wednesday is : {self.wednesday}")
            print(f"your subjects on thursday is : {self.thursday}")
students = Student2("economics","english","maths")
students.display()
