from z1 import student
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, Student):
        if isinstance(Student,student):
            self.students.append(Student)

    def remove_student(self, Student):
        if Student in self.students:
            self.students.remove(Student)
        else:
            print("Такого студента нет в списке.")

    def list_students(self):
        if not self.students:
            print("У преподавателя пока нет студентов.")
        else:
            print("Список студентов:")
            for i, student in enumerate(self.students, 1):
                print(f"{i}. {student.name}")


K = teacher("Ягами Лайт", 25, "Философия")
L = student("Эл Лоулайт", "999")
K.add_student(L)
K.list_students()
