def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]
lst2 = ajouter_elt(lst1, len(lst1))

print(f"La liste lst1 contient {lst1}, est de type {type(lst1)} et son identifiant est {id(lst1)}")
print(f"La liste lst2 contient {lst2}, est de type {type(lst2)} et son identifiant est {id(lst2)}")
