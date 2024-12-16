list = [3,7,5,7,8,1,10]

for i in list:
    listNew = []
    x = lambda a : a > 5
    print(x(i))
    if x(i) == True:
        listNew.append(i)
        print(listNew)

print(listNew)