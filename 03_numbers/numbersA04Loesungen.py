from decimal import Decimal

from unicodedata import decimal

prices = [52.43, 12.46, 21.54, 10.00, 76.45, 76.54, 99.21, 33.21, 11.33, 43.65]
priceSum = 0

for price in prices:
    priceSum = priceSum + Decimal(price)

priceSum = round(priceSum, 2)
print(priceSum)