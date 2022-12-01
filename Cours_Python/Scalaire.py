nMax = 10

v1 = []
v2 = []
prodScal = 0
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

while not(n >= 1 and n <= 10):
    n = int(input("Merci d'entrer une taille valide pour les vecteurs [entre 1 et 10] : "))

print("\nSaisie du premier vecteur :")
for i in range(0, n):
    x = int(input(f"v1[{i}] = "))
    v1.append(x)

print("\nSaisie du second vecteur :")
for i in range(0, n):
    x = int(input(f"v2[{i}] = "))
    v2.append(x)

for i in range(0, n):
    prodScal += float((v1[i] * v2[i]))

print(f"Le produit scalaire de v1 par v2 vaut {prodScal}")