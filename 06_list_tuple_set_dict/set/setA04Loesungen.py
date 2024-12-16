a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
updateList = []

nurInA = a.symmetric_difference(b)
for i in nurInA:
    if i in b:
        updateList.append(i)

for i in updateList:
    nurInA.remove(i)

updateList.clear()

nurInB = b.symmetric_difference(a)
for i in nurInB:
    if i in a:
        updateList.append(i)

for i in updateList:
    nurInB.remove(i)

print(nurInA, nurInB)