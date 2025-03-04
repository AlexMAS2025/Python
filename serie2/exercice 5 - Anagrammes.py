import random
import string

words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]
cards = tuple()

user = input("Entrez un mot :")

print(f'mots possedant {user}')
wordsList = list(w for w in words if sorted(w) == sorted(user)) #letter in w : vérifie lettre présent dans w

print (wordsList)