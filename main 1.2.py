"""
Author: Martin Calamel
Created: 2024-10-03
Description: fichier principal pour le pendu version 1 invite de commande
TODO: faire la deuxième vesion de l'invite de commande:
        • qu’il précise au joueur s’il donne une lettre déjà donnée auparavant
        • qu’il propose au joueur de rejouer en fin de partie
        • qu’il retienne le meilleur score des parties déjà jouées.
"""
from fonction import tour, select_mystery
from os import system

system("cls")
jouer = True
meilleur_score = 0

while jouer:
    mot_mystere = select_mystery()
    gagne = False
    perdu = False
    vie = 8
    mot_en_cours = mot_mystere[0]+"_"*(len(mot_mystere)-1)
    lettres_teste = []
    while not gagne and not perdu:
        print(mot_en_cours, '\n\nVies : ', vie, "/8")
        print("\n",lettres_teste,"\n")
        saisie = input("lettre ou mot en majuscule pour le pendu \n>>> ")
        if saisie in lettres_teste:
            print("lettre déjà tester")
        
        else:
            lettres_teste.append(saisie)
            mot_en_cours, vie, gagne, perdu, saisie, = tour(saisie, mot_mystere, mot_en_cours, vie)
            if not saisie:
                print("veilliez à respecter les consignes de saisie")
        system("cls")
    
    if gagne:
        print(mot_en_cours)
        print("Bravo vous avez gagné !!!")
        print("score = ", vie)
        if vie > meilleur_score:
            meilleur_score = vie
            print("nouveau meilleur score !!!")
    
    else:
        print("Vous avez perdu...")
        print("le mot était : ", mot_mystere)
    jouer= input("voulez vous continuer a jouer (Y/N) : ") == "Y"
        
