import time
n = int(input("Entrez un nombre : "))
x = 0
while n <= 0:
    n = int(input("Merci d'entrer un nombre valide : "))
for i in range(0, n+1):
    time.sleep(0.5)
    print(n - x)
    x += 1