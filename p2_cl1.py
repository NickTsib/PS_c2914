class Student:
    print("Hi!")
    def __init__(self, height=160):
        self.height = height


vasya = Student()
print(vasya.height)

dima = Student(height=186)
print(dima.height)

