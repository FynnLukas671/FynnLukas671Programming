def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n >= 3:
        return fibonacci(n-1)+fibonacci(n-2)
def main():
    print(fibonacci(int(input("Geben sie eine Zahl an: "))))
    main()
main()