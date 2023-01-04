dictionnaire = {}
dictionnaire['name'] = input("Entrez votre nom : ")
dictionnaire['firstname'] = input("Entrez votre prénom : ")
dictionnaire['promo'] = input("Entrez votre promotion : ")
dictionnaire['group'] = input("Entrez votre groupe de tp : ")

print(f"\nvotre nom est {dictionnaire['name']}, prénom est {dictionnaire['firstname']}, vous faites partie de la promo {dictionnaire['promo']} et votre group est {dictionnaire['group']}")

keys = list(dictionnaire.keys())
values = list(dictionnaire.values())
pairs = list(dictionnaire.items())

print("\nLes clés du dictionnaire sont :")
for i in range(0, 4):
    print(f"- {keys[i]}")

print("Les valeurs du dictionnaire sont :")
for i in range(0, 4):
    print(f"- {values[i]}")

print("Les tuplets du dictionnaire sont :")
for i in range(0, 4):
    print(f"- {pairs[i]}")

dictionnaire2 = {}
dictionnaire2['name'] = input("\nEntrez le nom du binome : ")
dictionnaire2['firstname'] = input("Entrez le prénom du binome : ")
dictionnaire2['promo'] = input("Entrez la promotion du binome : ")
dictionnaire2['group'] = input("Entrez le groupe de tp du binome : ")

binôme = {}
binôme['etu1'] = dictionnaire
binôme['etu2'] = dictionnaire2

print("\nLes étudiants formants le binôme sont :")
print(f"- L'étudiant {binôme['etu1']['name']} {binôme['etu1']['firstname']} du groupe {binôme['etu1']['group']}")
print(f"- L'étudiant {binôme['etu2']['name']} {binôme['etu2']['firstname']} du groupe {binôme['etu2']['group']}")