hausaufgaben = int(input("Hast du deine Hausaufgaben gemacht?(1/0) "))
mathNote = int(input("Welche Note hattest du in Mathe? "))

if hausaufgaben == True and mathNote >= 70:
    print("YAY!!! Du bekommst eine Belohnung!!!")
else:
    print("Wow. Du Loser...")