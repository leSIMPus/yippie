from z1 import student
from z2 import teacher

class Assistant(student, teacher):
    def __init__(self, name, student_id, age, subject):
        student.__init__(self, name, student_id)
        teacher.__init__(self, name, age, subject)

    def help_student(self):
        print(f"{self.name} помогает другим студентам учиться по предмету {self.subject}.")


A = Assistant("Антон Гогуев", "17", 19, "Программирование")
A.add_student(student("Елизавета Пронина", "15"))
A.add_grade(10)
A.add_grade(10)
A.add_grade(10)
A.display_info()
A.list_students()
A.help_student()