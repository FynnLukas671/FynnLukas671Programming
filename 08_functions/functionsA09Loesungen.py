def main(mode):
    if mode == 1:
        hello()
    elif mode == 2:
        x = int(input("Geben sie eine Zahl an: "))
        y = int(input("Geben sie eine weitere Zahl an: "))
        multiply(x,y)
    elif mode == 3:
        x = int(input("Welche Zahl soll geprüft werden? "))
        greaterZero(x)
    elif  mode== 4:
        endProgram()
    else:
        main(int(input("Geben sie den Zustand des Programms an: (1/2/3/4)")))

def hello():
    print("Hello!")
    main(int(input("Geben sie den Zustand des Programms an: (1/2/3/4)")))

def multiply(x,y):
    print(x*y)
    main(int(input("Geben sie den Zustand des Programms an: (1/2/3/4)")))

def greaterZero(x):
    if x > 0:
        print(f"{x} is greater than zero.")
    else:
        print(f"{x} is less than zero.")
    main(int(input("Geben sie den Zustand des Programms an: (1/2/3/4)")))

def endProgram():
    print("End of Programm!")

main(int(input("Geben sie den Zustand des Programms an: (1/2/3/4)")))