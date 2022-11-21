BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Combien y a-t-il de convives ? "))
nvfromage = (fromage * nbConvives) / BASE
nveau = (eau * nbConvives) / BASE
nvail = (ail * nbConvives) / BASE
nvpain = (pain * nbConvives) / BASE
print(f"Pour faire une fondu pour {nbConvives} personnes, il vous faut:")
print(f"- {nvfromage:.2f} grammes de fromage")
print(f"- {nveau:.1f} dl d'eau")
print(f"- {nvail:.1f} gousse(s) d'ail")
print(f"- {nvpain:.2f} gr de pain")
