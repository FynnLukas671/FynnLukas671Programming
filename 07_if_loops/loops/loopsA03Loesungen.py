notenListe = list()
gradesTotal = 0
eingabe = 1

while eingabe != "stop":
    eingabe = str(input("Wie lautet ihre letzte Note? "))
    filter = eingabe
    if eingabe != "stop":
        notenListe.append(eingabe)
        print(notenListe)

for i in notenListe:
    gradesTotal = gradesTotal + int(i)

gradeAverage = gradesTotal / len(notenListe)

print(gradeAverage)