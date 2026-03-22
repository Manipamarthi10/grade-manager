class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest(self):
        if not self.grades:
            return 0
        return max(self.grades)

    def lowest(self):
        if not self.grades:
            return 0
        return min(self.grades)

    def is_passing(self):
        return self.average() >= 40

    def grade_letter(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
