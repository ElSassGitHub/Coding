notes = {}
somme = 0
totalcoef = 0
admis = True

for i in range(0, 5):
    valeurs = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant : ")
    temp = valeurs.split(" ")
    notes[f'module {i + 1} note'] = float(temp[0])
    notes[f'module {i + 1} coef'] = int(temp[1])

for i in range(0, 5):
    if notes[f'module {i + 1} note'] < 8:
        admis = False
        break
    else:
        somme += notes[f'module {i + 1} note'] * notes[f'module {i + 1} coef']
        totalcoef += notes[f'module {i + 1} coef']

if admis == False:
    print("Etudiant non admis")
else:
    moyenne = somme / totalcoef
    if moyenne > 10:
        admis = True
        print("Etudiant admis")
