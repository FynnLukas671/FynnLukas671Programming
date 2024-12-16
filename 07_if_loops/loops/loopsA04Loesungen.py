eingabe = 1
gradeDict = {1: "Sehr gut",
             2: "Gut",
             3: "Befriedigend",
             4: "Ausreichend",
             5: "Mangelhaft",
             6: "Ungenügend"}
gradeList = gradeDict.keys()

while eingabe != "stop":
    eingabe = str(input("Wie lautet ihre letzte Note? "))

    if eingabe != "stop":

        for i in gradeList:

            if int(eingabe) == i:
                print(gradeDict[i])