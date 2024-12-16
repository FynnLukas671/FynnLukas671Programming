from datetime import datetime

now = datetime.today()
specialDate = str(input("Geben sie ein Datum an: "))
specialDate = datetime.strptime(specialDate, "%d.%m.%Y")
print(specialDate)

timeToWait = now - specialDate

hours = timeToWait.seconds // 3600
minutes = timeToWait.seconds % 3600 // 60

print(f"That was {timeToWait.days} days, {hours} hours and {minutes} minutes ago.")