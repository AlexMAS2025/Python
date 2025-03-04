def mediane(*numbers):
    ordered = sorted(numbers)
    n = len(ordered)
    if n % 2 == 1:
        return ordered[(n-1)//2]
    else:
        half = n // 2
        return (ordered[half-1] + ordered[half]) / 2

numbers = ()
print('Entrez un nombre par ligne, ligne vide pour terminer.')

while True:
    n = input()
    if n.strip() == "":
        break
    numbers += (float(n),)

print(f'Vous avez entré {len(numbers)} nombres; leur mediane est {mediane(*numbers):.2f}')