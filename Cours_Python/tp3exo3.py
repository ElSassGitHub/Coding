import random
val_cible = random.randrange(0, 101)
compteur = 0
while True:
    essai = int(input("Entrez un nombre : "))
    compteur += 1
    if essai > val_cible:
        print("La valeur est plus petite")
    elif essai < val_cible:
        print("La valeur est plus grande")
    else:
        break
print(f"\nBravo ! La valeaur est bien {essai}")
print(f"Cela vous a prit {compteur} tours")