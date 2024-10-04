"""
Author: Martin Calamel
Created: 2024-10-03
Description: pendu avec interface graphique 
TODO: faire l'interface
      faire la communication avec les fonctions
"""

import tkinter
import tkinter.messagebox
from fonction import tour, select_mystery
from PIL import Image,ImageTk

# fonction

def open_image(img_name: str):
    '''
    fonction pour ouvire une image en temps que variable utilisable par tkinter

    #input: nom de l'image (str)
    #output: image ouverte pour tkinter
    '''

    image = ImageTk.PhotoImage(Image.open(img_name))
    return image

def open_all_image(liste_name):
    '''
    fonction pour ouvrire toutes les images a partire d'une liste de nom

    #input: liste des nom (list)
    #output: liste d'image tkinter (list)
    '''

    liste_image = [open_image(i) for i in liste_name]
    return liste_image

def victory(gagne: bool) -> None:
    '''
    fonction pour afficher le message en cas de victoire

    #input: est ce que victoire ? (bool)
    #output: rien (None)
    '''

    if gagne:
        tkinter.messagebox.showinfo('Victoire',"Vous avez gagné")

def loose(perdu: bool) -> None:
    '''
    fonction pour afficher le message en cas de défaite

    #input: est ce que défaite ? (bool)
    #output: rien (None) 
    '''
    if perdu:
        tkinter.messagebox.showwarning('Défaite',"Vous avez perdu\n le mot était "+str(mot_mystere))

def error(saisie: bool) -> None:
    '''
    fonction pour afficher le message en cas d'erreur de saisie

    #input: est ce que erreur ? (bool)
    #output: rien (None)
    '''
    if not saisie:
        tkinter.messagebox.showerror('erreur',"Veuillez vous conformer au règles de saisie")

def reset():
    '''
    fonction pour recommencer une partie et remette les variable au condition initial

    #input: rien
    #output: rien
    '''
    global mot_mystere, mot_en_cours, gagne, perdu, vie, image_container
    mot_mystere = select_mystery()
    mot_en_cours = mot_mystere[0]+"_"*(len(mot_mystere)-1)
    gagne = False
    perdu = False
    vie = 8
    image_container = canvas.create_image(10,10,anchor=tkinter.NW,image=liste_image[0])
    label_mot_courant.config(text= mot_en_cours)
    label_vie_restante.config(text= "Vies restantes : " + str(vie))

def states(gagne, perdu, saisie):
    '''
    fonction pour gérer les états en fin de tours

    #input: états de gagne (bool), états de perte (bool), états de saisie (bool) 
    #output: rien (None)
    '''
    victory(gagne)
    loose(perdu)
    error(saisie)
    if gagne or perdu:
        res=tkinter.messagebox.askquestion('Exit Application', 'voulez vous jouer une nouvelle partie')
        if res == "yes":
            reset()
        else :
            fen.destroy()

def switch_image(vie):
    canvas.itemconfig(image_container,image=liste_image[7-vie])


def play_tour(event=None):
    global vie, mot_en_cours, mot_mystere
    saisie=entry_saisie.get()
    entry_saisie.delete(0, 'end')
    mot_en_cours, vie, gagne, perdu, saisie, = tour(saisie, mot_mystere, mot_en_cours, vie)
    label_mot_courant.config(text= mot_en_cours)
    label_vie_restante.config(text= "Vies restantes : " + str(vie))
    switch_image(vie)
    states(gagne,perdu,saisie)
    

# variable globales
mot_mystere = select_mystery()
mot_en_cours = mot_mystere[0]+"_"*(len(mot_mystere)-1)
gagne = False
perdu = False
vie = 8

# config fenêtre

fen = tkinter.Tk()
liste_name_image = ["images_PENDU/bonhomme"+str(i+1)+".gif" for i in range(8)]
liste_image = open_all_image(liste_name_image)

# élément de la fenêtre

label_mot_courant = tkinter.Label(fen, text= mot_en_cours)
label_mot_courant.grid(row = 0, column= 0, columnspan= 2)

label_vie_restante = tkinter.Label(fen, text= 'Vies restantes : ' + str(vie))
label_vie_restante.grid(row= 1, column= 0, columnspan= 2)

entry_saisie = tkinter.Entry(fen)
entry_saisie.bind("<Return>",play_tour)
entry_saisie.grid(row= 2, column= 0)

bouton_valide = tkinter.Button(fen, text= 'Soumettre', command= play_tour)
bouton_valide.grid(row= 2, column= 1)

canvas = tkinter.Canvas(fen, width= 400, height= 400)
canvas.grid(row=0, column=3, rowspan= 10)
image_container = canvas.create_image(10,10,anchor=tkinter.NW,image=liste_image[0])


fen.mainloop()
