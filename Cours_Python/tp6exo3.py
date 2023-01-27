def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

def ajouter_carac(ch="abc", elt="d"):
    temp = ch + elt
    return temp

print(ajouter_elt(), id(ajouter_elt))
print(ajouter_carac(), id(ajouter_carac()))
