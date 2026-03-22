class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)  # BUG: crashes if grades is empty

    def highest(self):
        return max(self.grades)  # BUG: crashes if grades is empty

    def lowest(self):
        return min(self.grades)  # BUG: crashes if grades is empty

    def is_passing(self):
        return self.average() > 40  # BUG: should be >= 40 not >

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
