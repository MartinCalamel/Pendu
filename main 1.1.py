"""
Author: Martin Calamel
Created: 2024-10-03
Description: fichier principal pour le pendu version 1 invite de commande
TODO: faire la première vesion de l'invite de commande:
        - Choisit au hasard un mot dans un fichier constitué par vos soins. Dans ce fichier, les mots
        sont classés par taille puis par ordre alphabétique.
        - Affiche la première lettre du mot et des underscore (_) pour les autres lettres qui sont
        différentes
        - Laisse 8 chances au joueur pour deviner le mot. 
"""
from fonction import tour, select_mystery
from os import system

system("cls")
jouer = True

while jouer:
    mot_mystere = select_mystery()
    gagne = False
    perdu = False
    vie = 8
    mot_en_cours = mot_mystere[0]+"_"*(len(mot_mystere)-1)
    lettre_teste=[]

    while not gagne and not perdu:
        print(mot_en_cours, '\nVie : ', vie, "/8")
        print(lettre_teste,"\n")
        saisie = input("lettre ou mot en majuscule pour le pendu \n>>> ")
        lettre_teste.append(saisie)
        mot_en_cours, vie, gagne, perdu, saisie, = tour(saisie, mot_mystere, mot_en_cours, vie)
        if not saisie:
            print("veilliez à respecter les consignes de saisie")
        system("cls")
    
    if gagne:
        print("Bravo vous avez gagner !!!")
    
    else:
        print("Vous avez perdu...")

    jouer= input("vouler vous continuer a jouer (Y/N) : ") == "Y"
        
