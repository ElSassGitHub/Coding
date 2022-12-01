nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0
notes = []
print("\n")

for i in range(0, nombreEtudiants):
    x = float(input(f"Note étudiant {i} : "))
    while not (x > 20 and x < 0):
        x = float(input(f"Entrez une note valide pour l'étudiant {i} : "))
    notes.append(x)
    moyenne += x

moyenne = moyenne / nombreEtudiants

print(f"\nMoyenne de classe : {moyenne}")
print("\nNuméro de l'étudiant | note | écart à la moyenne")

for i in range(0, nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i] - moyenne}")