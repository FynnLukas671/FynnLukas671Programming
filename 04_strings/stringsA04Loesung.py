original = float(input("Geben sie einen Geldbetrag an: "))
discount = int(input("Geben sie einen Prozentsatz an: "))

endPrice = original - original * ( discount / 100 )

print(f"Originalpreis: {original}, Rabatt: {discount}%, Endpreis: {endPrice} €")