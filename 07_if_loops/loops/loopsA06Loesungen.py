from time import sleep

timer = int(input("Geben sie den Countdown an: "))

while timer >= 0:
    print(timer)
    timer -= 1
    sleep(1)

print("Boom!!!")