import re
sentence = str(input("Geben sie einen Satz ein: "))

words = re.split(" ", sentence)
wordCount = len(words)

print(sentence.upper(), len(sentence), wordCount)