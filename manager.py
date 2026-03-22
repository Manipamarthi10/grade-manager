from student import Student


class GradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        self.students[name] = Student(name, grades)

    def get_student(self, name):
        return self.students[name]  # BUG: KeyError if student doesn't exist

    def class_average(self):
        totals = [s.average() for s in self.students.values()]
        return sum(totals) / len(totals)  # BUG: crashes if no students

    def top_student(self):
        return max(self.students.values(), key=lambda s: s.average())  # BUG: crashes if empty

    def failing_students(self):
        return [s.name for s in self.students.values() if not s.is_passing()]

    def add_grade(self, name, grade):
        self.students[name].grades.append(grade)  # BUG: KeyError if student doesn't exist
