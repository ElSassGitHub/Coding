start = int(input("Donnez l'heure de début de la location (un entier) : "))
end = int(input("Donnez l'heure de fin de la location (un entier) : "))

heures_low = 0
heures_high = 0
tarif_low = 0
tarif_high = 0

while start < 0 or start > 24 or end < 0 or end > 24:
    print("Les heures doivent être comprises entre 0 et 24 !\n")
    start = int(input("Donnez l'heure de début de la location (un entier) : "))
    end = int(input("Donnez l'heure de fin de la location (un entier) : "))

while start == end:
    print("Attention ! L'heure de fin est identique à l'heure de début.\n")
    start = int(input("Donnez l'heure de début de la location (un entier) : "))
    end = int(input("Donnez l'heure de fin de la location (un entier) : "))

while start > end:
    print("Attention ! Le début de la location est après la fin ...\n")
    start = int(input("Donnez l'heure de début de la location (un entier) : "))
    end = int(input("Donnez l'heure de fin de la location (un entier) : "))

for i in range(start, end+1):
    if i > 7 and i <= 17:
        heures_high += 1
        tarif_high += 2
    else:
        heures_low += 1
        tarif_low += 1

print(f"Vous avez loué votre vélo pendant")
if heures_low != 0:
    print(f"{heures_low} heure(s) au tarif horaire de 1.0 euro(s)")
if heures_high != 0:
    print(f"{heures_high} heure(s) au tarif horaire de 2.0 euro(s)")
print(f"Le montant total à payer est de {tarif_high + tarif_low:.1f} euro(s).")