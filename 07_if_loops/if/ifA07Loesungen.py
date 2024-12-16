from random import randint

score1 = randint(1,6)
score2 = randint(1,6)

einsatz = float(input("Mit welchem Einsatz wollen sie spielen? "))

if score1 + score2 <= 6:
    print("Du hast verloren!!!")
elif score1 + score2 >= 7 and score2 + score1 <= 9:
    print("Du bekommst deinen Einsatz zurück.")
elif score1 + score2 == 10:
    print("Du bekommst das doppelte deines Einsatzes zurück.")
elif score1 + score2 == 11:
    print("Du bekommst das dreifache deines Einsatzes zurück.")
elif score1 + score2 == 12:
    print("Du bekommst das vierfache deines Einsatzes zurück.")
print(score1 + score2)
