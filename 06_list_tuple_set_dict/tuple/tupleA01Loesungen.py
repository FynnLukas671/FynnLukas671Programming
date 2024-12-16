testTuple = ("Alice", 25, "Studentin")

#tuple[25] = 26 doesn't work
#but

updateList = list(testTuple)
updateList[1] = 26

testTuple = tuple(updateList)

print(testTuple)