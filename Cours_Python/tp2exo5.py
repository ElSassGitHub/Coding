number = int(input("Entrez un nombre entier: "))
if number > 0:
    signe = "positif"
elif number < 0:
    signe = "négatif"
else:
    signe = "zéro"

if (number % 2) == 0:
    parité = "pair"
else:
    parité = "impair"
print(f"Le nombre est {signe} et {parité}")