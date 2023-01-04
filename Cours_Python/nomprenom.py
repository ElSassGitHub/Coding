personne1 = {}
personne2 = {}

personne1['nom'] = input("Entrez le nom de personne 1 : ")
personne1['prenom'] = input("Entrez le prénom de personne 1 : ")

personne2['nom'] = input("Entrez le nom de personne 2 : ")
personne2['prenom'] = input("Entrez le prénom de personne 2 : ")

if (personne1['nom'] < personne2['nom']) or (personne1['nom'] == personne2['nom'] and personne1['prenom'] < personne2['prenom']):
    print(personne1['prenom'].capitalize(), personne1['nom'].upper())
    print(personne2['prenom'].capitalize(), personne2['nom'].upper())
else:
    print(personne2['prenom'].capitalize(), personne2['nom'].upper())
    print(personne1['prenom'].capitalize(), personne1['nom'].upper())
