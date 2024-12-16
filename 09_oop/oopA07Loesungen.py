from random import randint


class Boss():
    def __init__(self, name):
        self.name = name

    def openVault(self):
        difficulty = randint(1, 10)

        if difficulty <=5:
            task1 = "Erfolg"
            return f"task1: {task1}"
        else:
            task1 = "Gescheitert"
            return f"task1: {task1}"

class ItExpert():
    def __init__(self, name):
        self.name = name

    def hackSecurity(self):
        difficulty = randint(1, 10)

        if difficulty <=5:
            task2 = "Erfolg"
            return f"task2: {task2}"
        else:
            task2 = "Gescheitert"
            return f"task2: {task2}"

class SafeOpener():
    def __init__(self, name):
        self.name = name

    def crackVaultDoorOpen(self):
        difficulty = randint(1, 10)

        if difficulty <=5:
            task3 = "Erfolg"
            return f"task3: {task3}"
        else:
            task3 = "Gescheitert"
            return f"task3: {task3}"

class Safe():
    def __init__(self, task1, task2, task3):
        self.task1 = task1
        self.task2 = task2
        self.task3 = task3

    def getOpenBy(self):
        if self.task1 == "Erfolg" and self.task2 == "Erfolg" and self.task3 == "Erfolg":
            return "offen!!!"
        else:
            return "Gescheitert"

class SafeController():
    def initialization(self):
        b1 = Boss("Harald")
        i1 = ItExpert("Heiz")
        o1 = SafeOpener("Hermann")
        s1 = Safe(b1, i1, o1)

        i1.hackSecurity()
        o1.crackVaultDoorOpen()
        b1.openVault()
        s1.getOpenBy()

c1 = SafeController()

print(c1.initialization())