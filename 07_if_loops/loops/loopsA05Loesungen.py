import random

zufallsZahl = random.uniform(0, 1)
zufallsZahl = round(zufallsZahl, 2)
print(zufallsZahl)
guess = 3
versuche = 0

while guess != zufallsZahl:
    guess = float(input("Errate die Zahl: "))
    if guess == zufallsZahl:
        print("-----------------")
        print("YAY!!!")
    elif guess > zufallsZahl:
        print("Die Zahl ist kleiner")
    elif guess < zufallsZahl:
        print("Die Zahl ist größer")
    versuche += 1

print(f"Du hast {versuche} Versuche gebraucht um die Zahl zu erraten!")