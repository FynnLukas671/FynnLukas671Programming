students = ["Thomas", "Anna", "Mario", "Luigi", "Friedrich"]

grade = dict()
gradeAll = 0

grade.update({"Thomas":2})
grade.update({"Anna":2})
grade.update({"Mario":4})
grade.update({"Luigi":3})
grade.update({"Friedrich":1})

grades = grade.values()

for i in grades:
    gradeAll = gradeAll + i

gradeAverage = gradeAll / len(students)

print(gradeAverage)

for i in grade:
    if grade[i] > gradeAverage:
        print(i)