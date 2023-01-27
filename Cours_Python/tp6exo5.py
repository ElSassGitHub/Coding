def nettoyage(phrase):
    phrase2 = []
    alpha = []
    for i in range(0, len(phrase)):
        phrase[i].lower()
        phrase2.append(phrase[i])
    for i in range(0, len(phrase2)):
        if phrase2[i] in ["é", "è", "ê", "ë"]:
            phrase2[i] = "e"
        elif phrase2[i] in ["û", "ü", "ù"]:
            phrase2[i] = "u"
        elif phrase2[i] in ["à", "â", "ä"]:
            phrase2[i] = "a"
        elif phrase2[i] in ["î", "ï"]:
            phrase2[i] = "i"
        elif phrase2[i] == "ç":
            phrase2[i] = "c"
        if phrase2[i].isalpha() == True:
            alpha.append(phrase2[i])
    return alpha

def is_palindrome(phrase_nettoyée):
    palindrome = True
    test = phrase_nettoyée.copy()
    test.reverse()
    for i in range(0, len(phrase_nettoyée)):
        if phrase_nettoyée[i] != test[i]:
            palindrome = False
            break
    return palindrome

def _main_():
    entrée = input("Entrez un mot ou une phrase : ").lower()
    result = is_palindrome(nettoyage(entrée))
    if result == True:
        print("C'est un palindrome !")
    elif result == False:
        print("Ce n'est pas un palindrome")

_main_()