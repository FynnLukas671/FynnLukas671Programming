n = int(input("Fakultät von: "))
ergebnis = 1

# for i in range(1, n):
#     ergebnis = ergebnis + ergebnis * i

while n > 0:
    ergebnis = ergebnis * n
    n = n - 1

print(ergebnis)