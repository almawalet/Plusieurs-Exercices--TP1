import random

banniere = """
    #################################
            IFT-1004 AIRLINES
    #################################
"""
en_tete = "La meilleure compagnie aérienne au monde!"

print(banniere)
print(en_tete)

nombre_de_passagers = int(input("Combien de billets souhaitez-vous réserver ? : "))
somme = 0
for i in range (1, nombre_de_passagers+1):
    print(f"""
     ####################
        PASSAGER {i}/{nombre_de_passagers}
    #####################
    """)
    nom = input(f'Nom du passager {i}: ')
    age = int(input(f'Age du passager {i}: '))
    if age <= 3:
        prix_du_billet = 0
        somme = somme + prix_du_billet
        print(f'Prix du billet réservé pour {nom} : {prix_du_billet:.2f}$.')
    elif age >= 65:
        pourcentage_de_rabais = random.randint(15,55)
        rabais_en_dollars = (150*pourcentage_de_rabais)/100
        prix_du_billet = 150 - rabais_en_dollars
        somme = somme + prix_du_billet
        print(f'Rabais appliqué pour {nom} : {pourcentage_de_rabais}%.')
        print(f'Prix du billet réservé pour {nom} : {prix_du_billet:.2f}$.')
    else:
        prix_du_billet = 150
        somme = somme + prix_du_billet
        print(f'Prix du billet réservé pour {nom} : {prix_du_billet:.2f}$.')
if nombre_de_passagers != 0:
    print(f'Montant total à encaisser pour cette réservation : {somme:.2f}$.')

print("")

print("1. Enregistrer un autre client.")
print("2. Quitter")
choix = int(input("Entrez votre choix : "))
somme_total = somme
while choix !=2 :
    if choix == 1:
        somme_2 = 0
        print("")
        nombre_de_passagers = int(input("Combien de billets souhaitez-vous réserver ? : "))
        for i in range(1, nombre_de_passagers + 1): #J'ai fait un copie-coller de la boucle car l'énoncé du TP dit ne pas utiliser de fonction
            print(f"""
         ####################
            PASSAGER {i}/{nombre_de_passagers}
        #####################
        """)
            nom = input(f'Nom du passager {i}: ')
            age = int(input(f'Age du passager {i}: '))
            if age <= 3:
                prix_du_billet = 0
                somme_2 = somme_2 + prix_du_billet
                print(f'Prix du billet réservé pour {nom} : {prix_du_billet:.2f}$.')
            elif age >= 65:
                pourcentage_de_rabais = random.randint(15, 55)
                rabais_en_dollars = (150 * pourcentage_de_rabais) / 100
                prix_du_billet = 150 - rabais_en_dollars
                somme_2 = somme_2 + prix_du_billet
                print(f'Rabais appliqué pour {nom} : {pourcentage_de_rabais}%.')
                print(f'Prix du billet réservé pour {nom} : {prix_du_billet:.2f}$.')
            else:
                prix_du_billet = 150
                somme_2 = somme_2 + prix_du_billet
                print(f'Prix du billet réservé pour {nom} : {prix_du_billet:.2f}$.')
        if nombre_de_passagers != 0:
            print(f'Montant total à encaisser pour cette réservation : {somme_2:.2f}$.') #Fin du copier-coller
            somme_total = somme_total + somme_2
        print("")
        print("1. Enregistrer un autre client.")
        print("2. Quitter")
        choix = int(input("Entrez votre choix : "))
    if choix != 1 and choix!=2:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        print("")
        print("1. Enregistrer un autre client.")
        print("2. Quitter")
        choix = int(input("Entrez votre choix : "))
if choix == 2:
    print(f'Le montant total accumulé pour tous les clients est {somme_total:.2f}.')
    print("Bye, Bye!")

