import random

class Dice():
    def __init__(self, colour):
        self.__colour = colour
        self.__count = None

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def throwTheDice(self):
        self.__count = random.randint(1,6)

    def updateColour(self,colour):
        self.__colour = colour

    def countInWords(self):
        countDict = {1:"Eins",
                     2:"Zwei",
                     3:"Drei",
                     4:"Vier",
                     5:"Fuenf",
                     6:"Sechs"}

        for i in countDict.keys():
            if self.__count == i:
                return countDict[i]

    def results(self):
        self.throwTheDice()
        return self.__colour, self.countInWords()

    def __eq__(self, other):
        return self.__colour == other.__colour and self.__count == other.__count

    def __hash__(self):
        return hash((self.__colour, self.__count))

d1 = Dice(str(input('Geben sie eine Farbe an: ')))
d2 = Dice(str(input('Geben sie eine Farbe an: ')))

if d1.__hash__() == d2.__hash__():
    equalDices = True
else:
    equalDices = False

print(d1.results(), d2.results(), d1.__eq__(d2), equalDices)