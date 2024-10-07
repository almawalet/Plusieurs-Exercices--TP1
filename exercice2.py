hauteur = int(input("Entrez une hauteur : "))
if hauteur >= 4:
    for ligne in range(1, hauteur+1):
        for espace in range(1, hauteur-ligne+1):
            print(" ", end="")
        for colonne in range(1, ligne+1):
            print(f'{colonne}', end=" ")
        print ("")
else:
    print("Hauteur incorrecte.")