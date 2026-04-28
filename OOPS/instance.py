class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

s1 = Student("Arif")
print(s1.greet())
