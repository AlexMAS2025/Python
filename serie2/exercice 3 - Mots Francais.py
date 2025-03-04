# Chargement du fichier
words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

# 1) Nombre total de mots
total_words = len(words)

# 2) Nombre de mots de 4 lettres
four_letter_words = sum(1 for w in words if len(w) == 4)

# 3) Nombre de mots commençant par 'z'
words_starting_with_z = sum(1 for w in words if w.startswith('z'))

# 4) Nombre de mots contenant la lettre 'z'
words_containing_z = sum(1 for w in words if 'z' in w)

# 5) Nombre de mots commençant par 'a' et finissant par 's'
words_starting_a_ending_s = sum(1 for w in words if w.startswith('a') and w.endswith('s'))

# Affichage des résultats
print(f"Nombre total de mots : {total_words}")
print(f"Nombre de mots de 4 lettres : {four_letter_words}")
print(f"Nombre de mots commençant par 'z' : {words_starting_with_z}")
print(f"Nombre de mots contenant la lettre 'z' : {words_containing_z}")
print(f"Nombre de mots commençant par 'a' et finissant par 's' : {words_starting_a_ending_s}")