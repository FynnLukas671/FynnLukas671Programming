siebener1 = []
siebener2 = []
siebener3 = []

x = 7
while x <= 100:
    siebener1.append(x)
    x = x + 7

print(siebener1)

for i in range(len(siebener1)):
    i = i+1
    siebener2.append(7*i)

print(siebener2)

siebener3.extend(siebener2)
print(siebener3)