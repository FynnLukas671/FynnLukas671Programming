from datetime import datetime

now = datetime.today()
print(now)

specialDate = str(input("Geben sie ein Datum an: "))
specialDate = datetime.strptime(specialDate, "%d.%m.%Y")
print(specialDate)

timeToWait = specialDate - now

hours = timeToWait.seconds // 3600
minutes = timeToWait.seconds % 3600 // 60

print(f"You have to wait for {timeToWait.days} days, {hours} hours and {minutes} minutes.")