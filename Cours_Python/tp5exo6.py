T = input("Entrez un série de 100 caractères max : ")
length = 0

for i in range(0, 100):
    length += 1
    if T[i] == T[-1]:
        break

print(f"La chaîne est constituée de {length} caractères.")
