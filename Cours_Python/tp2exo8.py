x = float(input("Entrez un nombre réel: "))
if ((not x < -10) and (not x > -2)) or ((x > 0) and (not x > 1)) or ((not x < 2) and (x < 3)):
    print("x appartient à I")
else:
    print("x n'appartient pas à I")