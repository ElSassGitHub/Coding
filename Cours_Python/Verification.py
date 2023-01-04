import os.path
import datetime

fich1 = input("Entrez le nom du premier fichier : ")
fich2 = input("Entrez le nom du second fichier : ")

if os.path.isfile(fich1):
    print(f"\nLe fichier {fich1} existe et fait {os.path.getsize(fich1)} octets")
else:
    print(f"\nLe fichier {fich1} n'existe pas")

if os.path.isfile(fich2):
    print(f"Le fichier {fich2} existe et fait {os.path.getsize(fich2)} octets")
else:
    print(f"Le fichier {fich2} n'existe pas")

if os.path.getmtime(fich1) > os.path.getmtime(fich2):
    print(f"\n{fich1} est le plus récent, modifié le {datetime.datetime.fromtimestamp(os.path.getmtime(fich1))}")
else:
    print(f"\n{fich2} est le plus récent, modifié le {datetime.datetime.fromtimestamp(os.path.getmtime(fich2))}")
