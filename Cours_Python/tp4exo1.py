n = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

list = []

for i in range(0, 10):
    x = n * i
    list.append(x)

for i in range(0, 10):
    print(f"{n} * {i} = {list[i]:.1f}")