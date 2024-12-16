x = 125
werte = []

if x / 50 >= 1:
    werte.append(x//50)
    x = x % 50
    mode = 50
else:
    werte.append(0)

if x / 20 >= 1:
    werte.append(x//20)
    x = x % 20
    mode = 20
else:
    werte.append(0)

if x / 10 >= 1:
    werte.append(x//10)
    x = x % 10
    mode = 10
else:
    werte.append(0)

if x / 5 >= 1:
    werte.append(x//5)
    x = x % 5
    mode = 5
else:
    werte.append(0)

print(werte)
