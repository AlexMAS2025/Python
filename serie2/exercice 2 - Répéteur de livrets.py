import random

m1 = {}
for i in range(1, 11):
    for j in range(1, 11):
        m1[f"{i} x {j}"] = i * j

while True :
    print(f'nombre de livret restant : {len(m1)}')
    rand: int = random.randint(0, len(m1) - 1)
    clef, val = list(m1.items())[rand]
    print(clef)
    while True:
        usr = int(input(f'donnez le résultat: '))
        if usr == val:
            del m1[clef]
            break

