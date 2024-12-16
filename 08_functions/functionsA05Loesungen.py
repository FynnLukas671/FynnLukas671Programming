list = ["Mario", "Luigi", "Lorenzo", "Bad", "Dad"]

def upperCases(list):
    for i in list:
        index = list.index(i)
        list.insert(index, i.upper())
        list.remove(i)

def longerThanThree(list):
    smallerThree = []
    for i in list:
        if len(i) <=3:
            smallerThree.append(i)
    for i in smallerThree:
        list.remove(i)

upperCases(list)
longerThanThree(list)

print(list)