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

        - choisir un mot:
            #input :
            #output : un mot (str)

            - lecture de fichier:
                #input :
                #output : liste de mot (list)
            - choix du mot aléatoire:
                #input : 
                #output : mot (str)

        - fonction de verification saisie utilisateur:
            

            - vérifie que la saisie est bien une str:
                #input : saisie (str)
                #output : bool
            - vérifie qu'il n'y a pas de caractère spéciaux ni d'accent:
                #input : saisie (str)
                #output : validité (bool)
            - mettre la saisie en majuscule

        - fonction pour verifier la presence de la lettre dans le mot:
            #input : mot,lettre (str,str)
            #output : les position de la lettre [] si erreur (list)

        - fonction de remplacement de la lettre dans le mot:
            #input : liste des lettre, indices, lettre (list,list,str)
            #output : liste mise a jour

            -creation d'une liste de la taille du mot
            -placement au indice donner
"""
#importation des modules
from csv import reader
from random import choice





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
        content = reader(file,delimiter=';')
        data = [ligne[0] for ligne in content] # récupère le premier element de la ligne (seul)
        file.close()

        return data

def select_word() -> str:
    """
    prend le mot aléatoire pour le jeu du pendu dans un fichier (ici dictionnaire.txt) et le renvoie

    #input :
    #output : mot aléatoire (str)
    """

    liste_word = read_file("dictionnaire.txt")
    word = choice(liste_word)
    return word




##################################################################
#                         Tests unitaires                        #
##################################################################

if __name__ == "__main__":

    #fonction check_file

    print("check_file -> existance OK : ", check_file("dictionnaire.txt"))
    print("check_file -> existance NO : ", check_file("blabla.txt"))
    print("check_file -> mauvais format : ", check_file(12))

    #fonction read_file

    print("read_file -> existance OK : ", read_file("dictionnaire.txt"))
    print("read_file -> existance NO : ", read_file("blabla.txt"))
    print("read_file -> mauvais format : ", read_file(12))

    #fonction select_word

    print("select word -> word : ", select_word())
    print("select_word -> aléatoire : ")
    for i in range(10):
        print(select_word())
