heures = int(input("Entrez le nombre d'heures effectuées : "))
salaireH = int(input("Entrez le salaire horaire : "))
salaireF = 0

if heures > 200:
    retient = heures % 200
    salaireF += (retient * salaireH) * 1.5
    heures -= retient
if heures > 160:
    retient = heures % 160
    salaireF += (retient * salaireH) * 1.25
    heures -= retient
if heures <= 160:
    salaireF += heures * salaireH

print(f"Le salaire est égal à {salaireF}")