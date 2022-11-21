jour = int(input("Quel jour somme-nous ? "))
heure = int(input("Quelle heure est-il ? "))
minute = int(input("Quelle est la minuté actuelle ? "))
min_since = (jour * heure * 60) + minute
print(f"Depuis le début du mois, {min_since} minutes se sont écoulées")