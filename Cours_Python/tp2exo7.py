import random

number = random.randrange(0, 101)
if number < 66:
    résultat = "Pile"
else:
    résultat = "Face"

print(f"{résultat} !")