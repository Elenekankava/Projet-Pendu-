import random as rd
import tkinter as tk 

Listemots= {"3 ": ["coq", "ski", "jus", "nul","gaz", "axe", "rat", "feu", "mur", "sel", "bot", "tas", "lot", "jeu", "lac", "bol", "nid", "par", "riz", "mot", "vue", "but", "ton", "fin", "mer", "air", "sol", "don", "bar", "vue", "pis", "roc", "vie", "fer", "cap", "ron"],
            "4 ": ["beau", "joli", "thym", "yogi", "pion", "chat", "loup", "noir", "vert", "bleu", "port", "tour", "mont", "lait", "pain", "robe", "bain", "vent", "camp", "sole", "gris", "bois", "ciel", "dent", "faux", "rose", "pont", "doux", "cord", "film", "main", "pois", "vide", "clou", "fort"],
            "5 " : ["bruit", "cycle", "livre", "pomme", "tenue", "rugby", "table", "plage", "valse", "ferme", "ombre", "sable", "chute", "glace", "fleur", "porte", "verre", "moulin", "colis", "grille", "dalle", "piano", "tronc", "danse", "carte", "farce", "goule", "louve", "plain", "coeur", "train", "flute", "morce", "signe", "tigre", "phase"],
            "6 " : ["agneau", "alarme", "ananas", "arcade", "billet", "garage", "oiseau", "pierre", "valise", "tunnel", "fusain", "marais", "chemin", "barque", "forger", "cloche", "rapide", "soleil", "frambo", "gouter", "danser", "ranger", "fossil", "plante", "crayon", "bourse", "lamper", "bassin", "piston", "moulin", "courir", "lancer", "tordre", "filmer", "bercer", "manger", "chalet"],
            "7 " : ["puzzle", "abriter", "billard", "chariot", "crapaud", "fourmis", "iceberg", "valence", "clocher", "brasier", "lantern", "tranche", "pendule", "grenade", "cheveux", "voltage", "moteurs", "fenetre", "gourdin", "drapier", "saboter", "mystère", "plafond", "rempart", "baroque", "cascade", "lumiere", "bousier", "tresser", "marguer", "torrent", "siffler", "gravure", "palabre", "montage", "somnole", "travaux"], 
            "8 " : ["javelot", "losange", "spirale", "aquarium", "brocante", "diapason","objectif", "logiciel", "pastiche", "scorpion", "tabouret", "triangle", "utopique", "cascade", "boussole", "tornades", "panthère", "mystique", "tournage", "lumières", "fracture", "barbecue", "grenoble", "volcanes", "clarté", "chaleurs", "bourgeon", "printemps", "moulinet", "sauvages", "parfume", "fenêtres", "riviere", "mosaïque", "frissons", "tonnerre", "brouhaha", "marathon", "symphony", "cloporte", "moissons", "cascadeur", "periscope"]
}

import tkinter as tk
from functools import partial

def show_selection(choices, listbox):
    choices = choices.get()
    text=""
    for index in listbox.curselection():
        text += choices[index] + " "
    global mot
    mot = rd.choice(Listemots[str(text)])
    print(mot)
    return text


racine= tk.Tk()
label1=tk.Label(racine,text='nombre de lettres que vous voulez dans le mot', font='20')
choices = tk.Variable(racine, ('3', '4', '5','6'))
listbox = tk.Listbox(racine, listvariable=choices, selectmode="simple")
listbox.insert('end', '7', '8')
button = tk.Button(racine, text='Ok', command=partial(show_selection, choices, listbox))

label1.grid(column=0, row=0)
listbox.grid(row=1, column=0)
button.grid(row=2, column=0)
racine.destroy
racine.mainloop()
racine1=tk.Tk()




texte=tk.Label(racine1, text='')

def asterix (word) :
    word_l=list(word)
    nombre_asterix=len(word_l)
    affichage=' *  '*nombre_asterix
    texte.config(text=str(affichage), fg='black', font=30)
    
asterix(str(mot))

texte.grid(column=0, row= 10, columnspan=13)
racine1.mainloop()
#print(mot_en_asterix("manon"))
#dico = mot_en_asterix("manon")  #pas ouf l'idé


