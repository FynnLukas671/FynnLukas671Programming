zahlenMenge = {1, 2, 3, 4, 5, 6, 7}
teilMenge = {2, 3, 4}
updateMenge = set()

updateMenge.update(zahlenMenge)

for i in teilMenge:
    updateMenge.add(i)

if updateMenge == zahlenMenge:
    print(True)

