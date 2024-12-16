summe = 0

def add_numbers(a,b):
    global summe
    summe = summe + a + b
    print(summe)

add_numbers(int(input("Geben sie eine Zahl an: ")),int(input("Geben sie eine Zahl an: ")))
add_numbers(int(input("Geben sie eine Zahl an: ")),int(input("Geben sie eine Zahl an: ")))