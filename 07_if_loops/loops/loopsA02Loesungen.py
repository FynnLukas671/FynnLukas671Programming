for i in range(2,100):
    for j in range(2,100):
        if i != j and i % j == 0:
            filter = False
            break
        else:
            filter = True
    if filter == True:
        print(f"{i} ist eine Primzahl")