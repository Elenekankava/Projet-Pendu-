import random as rd
import tkinter as tk 

racine = tk.Tk()
texte=tk.Label(racine, text='')
def choix_mot(dico):
    global mot
    mot = rd.choice(dico)
    return mot 

def mot_en_asterix(word):
    dico={}
    word_l=list(word)
    print(word_l)
    for i in range (len(word_l)) :
        dico[str(word_l[i])]='*'
    return dico

def asterix (word) :
    word_l=list(word)
    nombre_asterix=len(word_l)
    affichage=' _  '*nombre_asterix
    texte.config(text=str(affichage), fg='black', font=30)
    
asterix('manon')

texte.grid(column=0, row= 10, columnspan=13)
racine.mainloop()
#print(mot_en_asterix("manon"))
#dico = mot_en_asterix("manon")  #pas ouf l'idé




