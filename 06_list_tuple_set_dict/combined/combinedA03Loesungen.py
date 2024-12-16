from datetime import datetime, date, timedelta
from random import randint

lottozahlen = list()
ergebnis = dict()
week = timedelta(weeks=1)

woche1 = datetime.now().date()
woche2 = woche1 + week
woche3 = woche1 + week * 2

daten = [woche1, woche2 , woche3]

def lottozahlenGenerator():
    random = randint(1, 49)

    if random in lottozahlen:
        lottozahlenGenerator()
    elif random not in lottozahlen:
        return random

for i in daten:
    lottozahlen.clear()
    for j in range(6):
        lottozahlen.append(lottozahlenGenerator())
    ergebnis[i] = lottozahlen

print(ergebnis)