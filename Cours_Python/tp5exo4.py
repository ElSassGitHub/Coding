billets_100 = 0
billets_50 = 0
billets_10 = 0
pièces_2 = 0
pièces_1 = 0

money = int(input("Entrez un montant : "))

while money >= 100:
    money -= 100
    billets_100 += 1
while money >= 50:
    money -= 50
    billets_50 += 1
while money >= 10:
    money -= 10
    billets_10 += 1
while money >= 2:
    money -= 2
    pièces_2 += 1
while money >= 1:
    money -= 1
    pièces_1 += 1

print(f"{money} euros, c'est donc {billets_100} billets de 100, {billets_50} de 50, {billets_10} de 10, {pièces_2} pièces de 2 et {pièces_1} pièces de 1")
