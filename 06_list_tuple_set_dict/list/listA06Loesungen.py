einkaufsliste = ["Apfel", "Banane", "Milch", "Eier", "Brot"]

print(einkaufsliste)

einkaufsliste.append("Käse")
einkaufsliste.append("Joghurt")
print(einkaufsliste)

einkaufsliste.remove("Milch")
print(einkaufsliste)

for i in einkaufsliste:
    if i == "Eier":
        print("YAY")