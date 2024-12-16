from datetime import date

now = date.today()
endOfYear = date(now.year, 12, 31)
timeToWait = endOfYear - now

print("Noch", timeToWait.days, "Tage bis Jahresende!")