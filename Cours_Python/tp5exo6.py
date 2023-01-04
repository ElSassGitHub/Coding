T = input("Entrez un série de 100 caractères max : ")
done = False
voy = 0
exist = False
compte = 0

for i in range(0, 100):
    if done == True:
        break
    try:
        if T[i] == True:
            done = False
    except IndexError:
        done = True
    length = i

print(f"La chaîne est constituée de {length} caractères.")

for x in range(0, length):
    if T[x] == "a" or T[x] == "e" or T[x] == "i" or T[x] == "o" or T[x] == "u":
        voy += 1

print(f"La série contient {((voy * 100) / length):.2f}% de voyelles")

for y in range(0, length):
    try:
        if exist == True and T[y] == "w" and T[y + 1] == "a" and T[y + 2] == "g" and T[y + 3] == "o" and T[y + 4] == "n":
            compte += 1
        if exist == False and T[y] == "w" and T[y + 1] == "a" and T[y + 2] == "g" and T[y + 3] == "o" and T[y + 4] == "n":
            print(f"La chaine 'wagon' existe et sa première occurence débute à l'élément {y + 1}")
            exist = True
            compte += 1
    except IndexError:
        pass

print(f"La chaine 'wagon' est présente {compte} fois dans cette série.")