import sys
if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) == 1:
        print(f"Pas assez d'arguments pour le script argument.py")
    elif len(sys.argv) > 1:
        for elt in range(0, len(sys.argv)):
            print(f"\t-> {elt}")
