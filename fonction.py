"""
AUTHOR: Martin Calamel
DATE: 19/09/2024
GOAL: faire les fonction nécessaire à un jeu du pendu
TODO:

règles du jeu :
    - le joueur doit trouver un mot en essayant de trouver les lettres qui le compose
    - déroulement d'une manche : 
        - le joueur connais la longueur du mot et en fonction de la difficulté:
            - la première lettre et la dernière
            - la première lettre
            - rien d'autre
        - la partie est finie quand le joueur devine le mot ou quand le pendu est completer
    - déroulement d'un tour : 
        - le joueur propose une lettre ou un mot:
            - si la proposition est un mot :
                - on vérifie qu'il est juste et on fait soit gagner soit on ajoute une etape au pendu
            - si c'est une lettre :
                - on vérifie que la lettre est dans le mot:
                    - si oui on la place autant de fois qu'elle est dans le mot
                    - sinon on ajoute une etape au pendu
                - si la lettre a deja ete jouer on le dit au joueur


fonction pour pouvoir jouer :

        # - choisir un mot:
        #     #input :
        #     #output : un mot (str)

        #     - lecture de fichier:
        #         #input :
        #         #output : liste de mot (list)
        #     - choix du mot aléatoire:
        #         #input : 
        #         #output : mot (str)

        # - fonction de verification saisie utilisateur:
            

        #     - vérifie que la saisie est bien une str:
        #         #input : saisie (str)
        #         #output : bool
        #     - vérifie qu'il n'y a pas de caractère spéciaux ni d'accent:
        #         #input : saisie (str)
        #         #output : validité (bool)
        #     - mettre la saisie en majuscule

        # - fonction pour verifier la presence de la lettre dans le mot:
        #     #input : mot,lettre (str,str)
        #     #output : les position de la lettre [] si erreur (list)

        - fonction de remplacement de la lettre dans le mot:
            #input : indices, mot (list,list,str)
            #output : liste mise a jour
        
        - fonction pour check si la lettre est bien dans le mot:
            #input : liste des indices
            #output : bool
        
        - fonction pour faire le jeu:
            -tours:
                - récupérer une saisie utilisateur
                -vérifier si c'est une lettre ou un mot:
                    -si c'est une lettre:
                        - vérifier que la lettre est dans le mot:
                            * ajouter la lettre
                            * enlever une vie
                        -test de gagne
                    -si c'est un mot:
                        - teste de gagne:
                            * fin
                            * enlever une vie
                

            -creation d'une liste de la taille du mot
            -placement au indice donner
"""
##################################################################
#                   importation des modules                      #
##################################################################

from csv import reader
from random import choice


##################################################################
#                   fonctions choix du mot                       #
##################################################################


def check_file(file_name: str) -> bool:
    """
    Fonction pour vérifier que le fichier est bien existant

    #input : nom du fichier a vérifier (str)
    #output : existence du fichier (bool)
    """
    if type(file_name) == str : 
        try:
            file_data = open(file_name)
            file_data.close()
            return True
        
        except FileNotFoundError:
            print("le fichier n'existe pas")
            return False

    else:
        print("mauvaise saisie du nom de fichier")
        return False

def read_file(file_name: str) -> list:
    """
    renvoi les données du fichier spécifier après avoir vérifier sont existence

    #input : nom du fichier (str)
    #output : données contenue dans le fichier (list)
    """
    if check_file(file_name):

        file = open(file_name,"r")
        content = file.read()
        data = content.split(";") # récupère le premier element de la ligne (seul)
        file.close()

        return data

def select_mystery() -> str:
    """
    prend le mot aléatoire pour le jeu du pendu dans un fichier (ici dictionnaire.txt) et le renvoie

    #input :
    #output : mot aléatoire (str)
    """

    liste_mystery = read_file("dictionnaire.txt")
    mystery = choice(liste_mystery)
    return mystery

##################################################################
#                fonctions saisie utilisateur                    #
##################################################################

def check_saisie(saisie: str) -> bool:
    """
    fonction qui vérifie si la saisie est bien une chaîne de character\n
    et si il n'y a pas de caractère spéciaux 

    #input : saisie de l'utilisateur (str)
    #output : syntaxe correct (bool)
    """
    if type(saisie) == str:
        if len(saisie) == 1:
            return saisie in "AZERTYUIOPQSDFGHJKLMWXCVBN"
        else :
            for lettre in saisie:
                if lettre not in "AZERTYUIOPQSDFGHJKLMWXCVBN" :
                    return False
            return True
    return False

##################################################################
#                fonctions propres au pendu                       #
##################################################################

def lettre_in_mystery(lettre: str, mystery: str) -> list:
    """
    fonction qui cherche si le lettre donnée est dans le mot mystère

    #input : lettre (str), mot mystère (str)
    #output : liste des indice ou apparaît la lettre dans le mot (list)
    """
    indices=[ i for i in range(len(mystery)) if lettre == mystery[i] ]
    return indices

def put_lettre_word(lettre: str, indice: list, word: str):
    """
    fonction de remplacement de la lettre dans le mot

    #input : indices, mot (list,list,str)
    #output : liste mise a jour
    """
    pass




##################################################################
#                         Tests unitaires                        #
##################################################################

if __name__ == "__main__":

    #fonction check_file

    print("check_file -> existence OK : ", check_file("dictionnaire.txt"))
    print("check_file -> existence NO : ", check_file("blabla.txt"))
    print("check_file -> mauvais format : ", check_file(12))
    print("\n\n")

    #fonction read_file

    print("read_file -> existence OK : ", read_file("dictionnaire.txt"))
    print("read_file -> existence NO : ", read_file("blabla.txt"))
    print("read_file -> mauvais format : ", read_file(12))
    print("\n\n")

    #fonction select_word

    print("select word -> word : ", select_mystery())
    print("select_word -> aléatoire : ")
    for i in range(10):
        print(select_mystery())
    print("\n\n")
    
    #fonction check_saisie

    print("check_saisie -> saisie mot OK :",check_saisie("BONJOUR"))
    print("check_saisie -> saisie lettre OK :",check_saisie("B"))
    print("check_saisie -> saisie lettre special :",check_saisie("é"))
    print("check_saisie -> mauvais type :",check_saisie(12))
    print("\n\n")

    #fonction lettre_in_word
    print("lettre_in_word -> 2 E dans ELEPHANT au indices 0 et 2 :",lettre_in_mystery("E","ELEPHANT"))
    print("lettre_in_word -> 0 Z dans ELEPHANT :",lettre_in_mystery("Z","ELEPHANT"))
    print("\n\n")
    
