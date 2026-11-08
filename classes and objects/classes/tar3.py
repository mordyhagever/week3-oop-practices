
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        average = sum(self.grades) / len(self.grades)
        return average

    def __str__(self):
        return f"{self.name} (average {self.average()})"


