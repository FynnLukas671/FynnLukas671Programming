sonnigInput = str(input("Ist es heute sonnig? "))
wochenendeInput = str(input("Ist heute wochende? "))

if sonnigInput == "Ja" or sonnigInput == "ja":
    sonnig = True
else:
    sonnig = False

if wochenendeInput == "Ja" or wochenendeInput == "ja":
    wochenende = True
else:
    wochenende = False

if sonnig == True and wochenende == True:
    print("Perfektes Wetter für einen Ausflug!")

elif sonnig == True and wochenende == False:
    print("Schönes Wetter, aber leider kein Wochenende.")

elif sonnig == False and wochenende == True:
    print("Schade, dass das Wetter schlecht ist, aber wenigstens ist Wochenende.")

elif sonnig == False and wochenende == False:
    print("Weder schönes Wetter, noch Wochenende.")