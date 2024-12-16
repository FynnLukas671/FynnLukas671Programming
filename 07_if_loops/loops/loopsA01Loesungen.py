n = int(input("Fakultät von: "))
ergebnis = 1

for i in range(1, n):
    ergebnis = ergebnis + ergebnis * i

for j in range(1, 8):
    loopVariable = f"This is iteration {j}"
    print(loopVariable)

print(ergebnis)