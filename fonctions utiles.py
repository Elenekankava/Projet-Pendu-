import random as rd
import tkinter as tk 

racine = tk.Tk()
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
print(mot_en_asterix("manon"))
dico = mot_en_asterix("manon")  #pas ouf l'idé




