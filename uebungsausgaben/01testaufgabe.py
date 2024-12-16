height = 8
for i in range(height):
    tree = (2*i+1)*"*"
    spaces = (height-i)*" "
    print(spaces + tree)


for i in range(2):
    print((height-1)*" "+3*"*")