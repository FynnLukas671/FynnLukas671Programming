year = int(input("Geben sie ein Jahr ein: "))
schaltjahr = False

if year % 4 == 0:
    schaltjahr = True

print(schaltjahr)