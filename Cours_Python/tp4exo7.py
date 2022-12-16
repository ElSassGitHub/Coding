binome = (input("Entrez le nom du premier étudiant : "), input("Entrez le nom du second étudiant : "))
print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

ans = input("Souhaitez-vous changez le binome en trinome ? (Y/N) ")
if ans == "Y":
    y = list(binome)
    y.append(input("Entrez le nom du troisième étudiant : "))
    binome = tuple(y)
    print(f"L'étudiant {binome[0]} est maintenant en trinome avec les étudiants {binome[1]} et {binome[2]}")