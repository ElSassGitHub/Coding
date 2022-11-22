X = int(input("Entrez un nombre : "))
somme = 0
while X <= 1:
    X = int(input("Merci d'entrer un nombre valide : "))
for i in range(0, X+1):
    somme += i
    if somme > X:
        break
print(f"Le plus grand nombre N est {i-1}")