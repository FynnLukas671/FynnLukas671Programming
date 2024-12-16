list = [1, 2, 3, 3, 6, 4, 78, 2]

def filter():
    updateList = []
    for i in list:
        if list.count(i) > 1:
            list.remove(i)

    list.sort()
    list.reverse()

    for i in list:
        if i < list[2]:
            updateList.append(i)

    for i in updateList:
        list.remove(i)

    print(list)

filter()