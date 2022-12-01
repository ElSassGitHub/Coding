L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

compteur1 = 0
compteur2 = 0
n2 = 0

L2 = L1.copy()
L2.sort()
L2.reverse()

print(L1)

for i in range(0, len(L2)):
    if L2[i] == L2[0]:
        compteur1 += 1
        e1 = i
    elif L2[i] != L2[0]:
        compteur2 += 1
        n2 = L2[i]
        if n2 != L2[i-1]:
            e2 = i - 1
            compteur2 -= 1
            break

if compteur1 == compteur2:
    if L1.index(L2[e1]) < L1.index(L2[e2]):
        mostFrequent = L2[e1]
        compteur = compteur1
    elif L1.index(L2[e1]) < L1.index(L2[e2]):
        mostFrequent = L2[e2]
        compteur = compteur2
else:
    mostFrequent = L2[e1]
    compteur = compteur1
    
print(f"Le nombre le plus fréquent est le : {mostFrequent} ({compteur} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
