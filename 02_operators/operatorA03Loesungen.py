x = int(input("Geben sie 0 oder 1 an: "))
y = int(input("Geben sie noch einmal 0 oder 1 an: "))
Hauptlicht = False
Zusatzlicht = False

if x == 1 and y == 1:
    Zusatzlicht = True
    Hauptlicht = True
elif x == 1 or y == 1:
    Zusatzlicht = True

print("Hauptlicht:", Hauptlicht, "Zusatzlicht:", Zusatzlicht)