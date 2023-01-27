import random

def generer(nb, min, max):
    list = []
    for i in range(0, nb):
        list.append(random.randint(min, max))
    return list

def combienInferieur(list, limit):
    count = 0
    for i in range(0, len(list)):
        if list[i] < limit:
            count += 1
    return count

nb = int(input("Combien de nombres voulez-vous générer ? "))
vmin = int(input("Quelle est la limite basse ? "))
vmax = int(input("Quelle est la limite haute ? "))
print(f"\nGénérer {nb} nombres entiers entre {vmin} et {vmax}\n")
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)

while True:
    seuil = str(input("\nVoulez-vous préciser le seuil ? ")).lower()
    if seuil == "oui" or seuil == "o":
        comp = int(input("Entrez la valeur du seuil : "))
        total = combienInferieur(tab, comp)
        break
    elif seuil =="non" or seuil == "n":
        comp = 30
        total = combienInferieur(tab, comp)
        break

print(f"\nIl y en a {total} inférieurs à {comp}")
