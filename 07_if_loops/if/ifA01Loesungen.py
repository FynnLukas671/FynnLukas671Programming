door1 = int(input("Geben sie den Status der Tür an: (1/0) "))
door2 = int(input("Geben sie den Status der anderen Tür an: (1/0) "))

if door1 == 1 and door2 == 1:
    print("Sicher")
elif door1 == 0 or door2 == 0:
    print("Warnung!!!")