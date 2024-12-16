kurse = {"Mathematik": ["Anna", "Ben"],
         "Informatik": ["Max", "Clara"],
         "Physik": ["Eva", "David"]
         }

print(kurse["Informatik"])

informatikTeilnehmer = kurse.get("Informatik")
informatikTeilnehmer.append("Felix")
kurse.update({"Informatik":informatikTeilnehmer})

print(kurse)