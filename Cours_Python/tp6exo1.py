L1 = [0]*3
print(f"L'objet L1 contient {L1} et est de type {type(L1)} et d'identifiant {id(L1)}\n")

for i in range(0, len(L1)):
    print(f"{L1[i]} est de type {type(L1[i])} et son identifiant est {id(L1[i])}")

L1[1] += 1
print(f"\nL'objet L1 modifié contient {L1} et est de type {type(L1)} et d'identifiant {id(L1)}\n")

for i in range(0, len(L1)):
    print(f"{L1[i]} est de type {type(L1[i])} et son identifiant est {id(L1[i])}")
