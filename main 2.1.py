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

# variable globales
mot_mystere = select_mystery()
mot_en_cours = mot_mystere[0]+"_"*(len(mot_mystere)-1)
gagne = False
perdu = False
vie = 8

# fonction
def victory(gagne):
    if gagne:
        tkinter.messagebox.showinfo('Victoire',"Vous avez gagné")

def loose(perdu):
    if perdu:
        tkinter.messagebox.showwarning('Défaite',"Vous avez perdu")

def error(saisie):
    if not saisie:
        tkinter.messagebox.showerror('erreur',"Veuillez vous conformer au règles de saisie")

def states(gagne, perdu, saisie):
    victory(gagne)
    loose(perdu)
    error(saisie)
    if gagne or perdu:
        fen.destroy()


def play_tour(event=None):
    global vie, mot_en_cours, mot_mystere
    saisie=entry_saisie.get()
    entry_saisie.delete(0, 'end')
    mot_en_cours, vie, gagne, perdu, saisie, = tour(saisie, mot_mystere, mot_en_cours, vie)
    label_mot_courant.config(text=mot_en_cours)
    label_vie_restante.config(text="Vies restantes : " + str(vie))
    states(gagne,perdu,saisie)

# config fenêtre

fen = tkinter.Tk()

# élément de la fenêtre

label_mot_courant = tkinter.Label(fen, text = mot_en_cours)
label_mot_courant.grid(row = 0, column= 0, columnspan = 2)

label_vie_restante = tkinter.Label(fen, text= 'Vies restantes : ' + str(vie))
label_vie_restante.grid(row= 1, column= 0, columnspan= 2)

entry_saisie = tkinter.Entry(fen)
entry_saisie.bind("<Return>",play_tour)
entry_saisie.grid(row=2, column=0)

bouton_valide = tkinter.Button(fen, text= 'Soumettre', command= play_tour())
bouton_valide.grid(row=2, column=1)



fen.mainloop()
