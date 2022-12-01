tab = []
N = int(input("Combien de nombres voulez-vous dans la liste ? "))

print("\n")
for i in range(0, N):
    x = int(input(f"Entrez le nombre {i} : "))
    tab.append(x)

print("\n")
for i in range(0, N):
    print(tab)
    small = tab[i]
    for j in range(i+1, N):
        if tab[j] < small:
            small = tab[j]
    temp1 = tab.index(tab[i])
    temp2 = tab.index(small)
    entre = tab[i]
    tab[temp1] = small
    tab[temp2] = entre