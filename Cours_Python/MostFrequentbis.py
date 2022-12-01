L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

L2 = L1.copy()
L2.sort()
L2.reverse()

print(L1)

for i in range(0,len(L2)):
    if L2[i] == L2[0]:
        n = L2[0]
        x = L2.count(n)
        y = L1.index(n)
    else:
        m = L2[i]
        x2 = L2.count(m)
        y2 = L1.index(m)
        if x2 == x and y2 < y:
            n = m
            x = x2
            y = y2

print(f"Le nombre le plus fréquent dans la liste est le : {n} ({x} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
