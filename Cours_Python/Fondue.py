BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
nvfromage = (fromage * nbConvives) / BASE
nveau = (eau * nbConvives) / BASE
nvail = (ail * nbConvives) / BASE
nvpain = (pain * nbConvives) / BASE
print(f"Pour faire une fondu fribourgeoise pour {nbConvives} personnes, il vous faut:")
print(f"- {nvfromage:.1f} grammes de fromage")
print(f"- {nveau:.1f} dl d'eau")
print(f"- {nvail:.1f} gousse(s) d'ail")
print(f"- {nvpain:.1f} gr de pain")
