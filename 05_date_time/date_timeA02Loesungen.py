from datetime import date

ageYear = int(input("Geben sie ihr Geburtsjahr an: "))
ageMonth = int(input("Geben sie ihren Geburtsmonat an: "))
ageDate = int(input("Geben sie den Tag in dem Monat an dem sie geboren sind: "))

age = date(ageYear, ageMonth, ageDate)
now = date.today()

difference = date(now.year - age.year + 1, now.month - age.month + 1, now.day - age.day + 1)

print(f"Your are {difference.year} Years and {difference.month} Months old")