class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Оценка должна иметь значение от 0 до 10.")

    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")

    # пятое задание ↓
    def __str__(self):
        return f"Студент: {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        if isinstance(other, student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades)
    # пятое задание ↑

if __name__ == "__main__":
    print()
    F = student("Фаридушка Джафарова", "8129839128391283001012238477269817439816279339128738719237923")
    F.add_grade(9)
    F.add_grade(10)
    F.add_grade(10)
    F.display_info()
    print()
    A = student("Алисик Летуновская","8129839128391283001012238477269817439816279339128738719237923")
    A.add_grade(9)
    A.add_grade(9)
    A.add_grade(10)
    A.display_info()
    print()
    P = student("Полиночка Лубенец", "228")
    P.add_grade(9)
    P.add_grade(10)
    P.add_grade(8)
    P.display_info()
    print()
    M = student("Мария Учаева", "1")
    M.add_grade(9)
    M.add_grade(8)
    M.add_grade(10)
    M.display_info()

    # пятое задание ↓
    print(F)
    print(f"Количество оценок: {len(F)}")
    print(f"Одинаковы ли ID студентов F и P? {F == P}")
    print(f"Одинаковы ли ID студентов F и A? {F == A}")

