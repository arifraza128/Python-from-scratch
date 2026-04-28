class Student:
    def __init__(self, name):
        self.name = name

name = input("enter name: ")

s = Student(name)
print("student name is", s.name)
