class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades if grades else []

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def highest(self):
        return max(self.grades) if self.grades else 0

    def lowest(self):
        return min(self.grades) if self.grades else 0

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