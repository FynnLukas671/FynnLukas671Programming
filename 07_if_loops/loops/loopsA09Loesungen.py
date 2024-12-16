mode = 0

while mode != 4:
    mode = int(input("Geben sie den Zustand des Programms an:(1/2/3/4) "))

    if mode == 1:
        print("Hello!")
    elif mode == 2:
        x = int(input("Geben sie eine Zahl an: "))
        y = int(input("Geben sie eine weitere Zahl an: "))
        print(x*y)
    elif mode == 3:
        x = int(input("Welche Zahl soll geprüft werden? "))
        if x > 0:
            print(f"{x} is greater than zero.")
        else:
            print(f"{x} is less than zero.")
    elif  mode== 4:
        print("End of Programm!")