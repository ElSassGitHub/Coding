small = 0
medium = 0
big = 0
for i in range(0,10):
    x = float(input("Entrez un nombre : "))
    while x < 0 or x > 20:
        x = float(input("Merci d'entrer un nombre valide : "))
    if 0 <= x < 10:
        small += 1
    elif 10 <= x < 15:
        medium += 1
    elif 15 <= x <= 20:
        big += 1
print(f"Il y a {small} petites valeurs.")
print(f"Il y a {medium} valeurs moyennes.")
print(f"Il y a {big} grandes valeurs.")