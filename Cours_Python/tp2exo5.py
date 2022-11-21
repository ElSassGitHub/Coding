number = int(input("Entrez un nombre entier: "))
if number > 0:
    signe = "positif"
elif number < 0:
    signe = "négatif"
else:
    signe = "zéro"

if (number % 2) == 0 and number != 0:
    parité = "et pair"
elif number == 0:
    parité = "(et il est pair)"
else:
    parité = "et impair"
print(f"Le nombre est {signe} {parité}")