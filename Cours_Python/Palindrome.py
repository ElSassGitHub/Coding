entrée = input("Entrez un mot ou une phrase : ").lower()
alpha = []
palindrome = True

for i in range(0, len(entrée)):
    if entrée[i].isalpha() == True:
        alpha.append(entrée[i])

test = alpha.copy()
test.reverse()

for i in range(0, len(alpha)):
    if alpha[i] != test[i]:
        palindrome = False
        break

if palindrome == True:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome")