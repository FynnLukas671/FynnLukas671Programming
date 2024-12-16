from random import randint

testList = list()
testSet = set()

for i in range(10):
    testList.append(randint(1,5))

testSet = set(testList)
testList = list(testSet)

print(testList)