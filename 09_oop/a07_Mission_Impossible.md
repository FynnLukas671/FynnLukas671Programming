# Aufgabe: Mission Impossible

- In dieser Aufgabe soll es darum gehen, einen Safe zu öffnen. Dies wird nur erfolgreich passieren wenn von einer Gaunerbande, bestehend aus dem Boss, dem IT Experten und dem SafeOpener (Hardware Experte), jeder seine Aufgabe erfolgreich abschließt.
- Erstellen Sie die Klassen `Boss`, `SafeOpener`, `ItExpert` und `Safe` und `SafeController`
- Die Klasse `SafeController` soll die zentrale Logik enthalten
- `SafeOpener`, `ItExpert` und `Boss` haben jeweils die Variable `name` (3 zufällige Namen). 
	- `SafeOpener` hat die Methode `crack_vault_door_open()`
	- `ItExpert` die Methode `hack_security`
	- `Boss` hat die Methode `openSafe`
	- Jede der Methoden gibt einen String mit "Erfolg" oder "Misserfolg" zurück, jeweils mit einer Wahrscheinlichkeit von 50%. Alternativ: Lösen mittels Boolean
- Die Klasse `Safe` enthält die Methode `get_opened_by()`, die drei String Werte als Variablen übernimmt und nur dann "Offen" ausgibt, wenn alle drei Parameter "Erfolg" beinhalten, ansonsten wird "Alarm" ausgegeben.
- Die Klasse `SafeController` initialisiert jeweils eine Instanz der Klassen und startet einen Versuch zum Öffnen des Safes.