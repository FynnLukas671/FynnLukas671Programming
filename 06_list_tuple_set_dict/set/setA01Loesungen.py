fruechte = {"Apfel", "Banane", "Kirsche", "Mango"}

fruechte.add("Orange")
print(fruechte)

fruechte.remove("Banane")
print(fruechte)

filter = False
for i in fruechte:
    if i == "Apfel":
        filter = True

print(filter)