zugangskarte = int(input("Hat der user eine gültige Zugangskarte?(1/0) "))
sicherheitscode = int(input("Hat der user einen sicherheitscode?(1/0) "))

if zugangskarte == 1 and sicherheitscode == 1:
    print("Der user hat Zugang zum Gebäude.")

else:
    print("Der user hat keinen Zugang zum Gebäude.")