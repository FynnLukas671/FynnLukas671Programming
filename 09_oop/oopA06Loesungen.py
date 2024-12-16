class House():
    def __init__(self, owner, houseType):
        self.owner = owner
        self.houseType = houseType

class Wolf():
    def __init__(self, name):
        self.name = name

    def blow(House,h):
        if h.houseType == "Stein" or h.houseType == "Stahl" or h.houseType == "Wolf":
            print("Haus steht!^^")
        else:
            print("OH NO")
            del h

class MainController():
    def script(self):
        h1 = House('Pfeifer', 'Stroh')
        h2 = House('Grunzer', 'Holz')
        h3 = House('Schlau', 'Stein')
        w1 = Wolf('Wolf')

        w1.blow(h1)
        w1.blow(h2)
        w1.blow(h3)

m = MainController()
m.script()