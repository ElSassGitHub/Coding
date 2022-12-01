while True:
	date = input("Entrez une date : ")
	if len(date) != 8:
		print("Date non valide")
	else:
		jour = int(date[0] + date[1])
		mois = date[2] + date[3]
		année = int(date[4] + date[5] + date[6] + date[7])
		if jour == 0 or mois == 0 or année == 0:
			print("Date non valide")
		else:
			break

if mois == "01" or mois == "03" or mois == "05" or mois == "07" or mois == "08" or mois == "10" or mois == "12":
    if jour > 31:
        print("Date invalide")
    else:
        print("Date valide")
elif not ((année % 4 == 0) and (année % 100 != 0)) or (année % 400 == 0):
    if jour > 30:
        print("Date invalide")
    else:
        print("Date valide")
else:
    if jour > 29:
        print("Date invalide")
    elif jour > 28:
        print("Date invalide")
    else:
        print("Date valide")