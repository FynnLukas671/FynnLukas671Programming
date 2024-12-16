telefonbuch = {"Anna": "12345",
               "Ben": "23456",
               }

if telefonbuch.setdefault("Clara") == None:
    telefonbuch["Clara"] = "12345"

print(telefonbuch)