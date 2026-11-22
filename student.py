"""Store and display student details using a Python class."""


class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_details(self):
        print("Student Details")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")


if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")
    student = Student(name, roll_number, course)
    student.display_details()
