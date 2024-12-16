word1 = str(input("Enter a word: "))
word2 = str(input("Enter another word: "))

def common_words(word1, word2):
    word1Letter = set()
    word2Letter = set()

    for letter in word1:
        word1Letter.add(letter)

    for letter in word2:
        word2Letter.add(letter)

    commonWords = word1Letter.intersection(word2Letter)

    print(commonWords, len(commonWords))

common_words(word1, word2)