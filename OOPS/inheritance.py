class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_student(self):
        print("Course:", self.course)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_teacher(self):
        print("Subject:", self.subject)


s1 = Student("Arif", 21, "Cloud Computing")
t1 = Teacher("Rahul", 35, "Mathematics")

print("Student Info:")
s1.show_details()
s1.show_student()

print("\nTeacher Info:")
t1.show_details()
t1.show_teacher()
