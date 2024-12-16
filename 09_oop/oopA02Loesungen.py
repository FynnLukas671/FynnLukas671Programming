class Car():
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def carInfo(self):
        return self.marke, self.modell, self.baujahr

c1 = Car("Cadillac", "Z1", 1976)

print(c1.carInfo())