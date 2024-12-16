import re

sentence = str(input("Geben sie einen Satz ein: "))
startLetters = ""
sentence = sentence.split()

for i in range(len(sentence)):
    startLetters = startLetters + sentence[i][0]

print(startLetters)