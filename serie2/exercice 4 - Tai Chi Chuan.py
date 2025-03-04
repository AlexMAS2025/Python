import random
import string

#Chargement de la liste
words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]
cards = tuple()

for i in range(1,5):
    lettre = random.choice(string.ascii_lowercase)
    cards += (lettre,)

print(f'mots commencant par \'{cards[0]}\' et possedant {cards[1:]}')
wordsList = list(w for w in words if (w.startswith(cards[0]) and all(letter in w for letter in cards[1:]))) #liste des mots commencant par cards[0] et contenant le reste

print (wordsList)
