#hoehe = int(input("Geben sie die Höhe de Baumes an: "))
hoehe = 3

hoeheRange = list(range(hoehe))
hoeheRangeReverse = hoeheRange.reverse()

i = 3

for j in hoeheRange:
        print(j * " " + (i - 1) * "*" + "*" + (i - 1) * "*" + j * " ")
        i = i - 1