n = int(input("Entrez un nombre : "))
x = 1
y = 1

choix = input("Voulez-vous utiliser la boucle 'for' ou la boucle 'while' : ")
while choix != "for" and choix != "while":
    choix = input("Merci d'entrer 'for' ou 'while' : ")

if choix == "for":
    for i in range(1, n+1):
        x *= i
        print(x)
    print(f"Le factoriel de {n} est {x}")
elif choix == "while":
    while n > 0:
        x *= y
        y += 1
        n -= 1
        print(x)
    print(f"Le factoriel de {n} est {x}")