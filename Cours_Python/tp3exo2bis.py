import time
n = int(input("Entrez un nombre : "))
x = 0
while n <= 0:
    n = int(input("Merci d'entrer un nombre valide : "))
while n >= 0:
    time.sleep(0.5)
    print(n)
    n -= 1