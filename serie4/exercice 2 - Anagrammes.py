import random
import string

words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]
cards = tuple()

for i in range(1,5):
    lettre = random.choice(string.ascii_lowercase)
    cards += (lettre,)

print(f'mots possedant {cards[0:]}')
wordsList = list(w for w in words if all(letter in w for letter in cards[0:]))

print (wordsList)