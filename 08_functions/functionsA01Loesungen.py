def square_numbers_list(n):
    list = []
    for i in range(1,n+1):
        list.append(i**2)
    return list

print(square_numbers_list(n = int(input("Geben sie eine tolle Zahl an: "))))