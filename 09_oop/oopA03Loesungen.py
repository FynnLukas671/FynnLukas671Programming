class Students():
    numberOfStudents = 0
    def __init__(self, name):
        self.name = name
        Students.numberOfStudents += 1

    def number(self):
        return Students.numberOfStudents

s1 = Students("Mario")
s2 = Students("Luigi")

print(Students.number(s1))
