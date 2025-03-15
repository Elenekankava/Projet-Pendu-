
Listemots= {"3": ["coq", "ski", "jus", "nul","gaz", "axe", "rat", "feu", "mur", "sel", "bot", "tas", "lot", "jeu", "lac", "bol", "nid", "par", "riz", "mot", "vue", "but", "ton", "fin", "mer", "air", "sol", "don", "bar", "vue", "pis", "roc", "vie", "fer", "cap", "ron"],
            "4": ["beau", "joli", "thym", "yogi", "pion", "chat", "loup", "noir", "vert", "bleu", "port", "tour", "mont", "lait", "pain", "robe", "bain", "vent", "camp", "sole", "gris", "bois", "ciel", "dent", "faux", "rose", "pont", "doux", "cord", "film", "main", "pois", "vide", "clou", "fort"],
            "5" : ["bruit", "cycle", "livre", "pomme", "tenue", "rugby", "table", "plage", "valse", "ferme", "ombre", "sable", "chute", "glace", "fleur", "porte", "verre", "moulin", "colis", "grille", "dalle", "piano", "tronc", "danse", "carte", "farce", "goule", "louve", "plain", "coeur", "train", "flute", "morce", "signe", "tigre", "phase"],
            "6" : ["agneau", "alarme", "ananas", "arcade", "billet", "garage", "oiseau", "pierre", "valise", "tunnel", "fusain", "marais", "chemin", "barque", "forger", "cloche", "rapide", "soleil", "frambo", "gouter", "danser", "ranger", "fossil", "plante", "crayon", "bourse", "lamper", "bassin", "piston", "moulin", "courir", "lancer", "tordre", "filmer", "bercer", "manger", "chalet"],
            "7" : ["puzzle", "abriter", "billard", "chariot", "crapaud", "fourmis", "iceberg", "valence", "clocher", "brasier", "lantern", "tranche", "pendule", "grenade", "cheveux", "voltage", "moteurs", "fenetre", "gourdin", "drapier", "saboter", "mystère", "plafond", "rempart", "baroque", "cascade", "lumiere", "bousier", "tresser", "marguer", "torrent", "siffler", "gravure", "palabre", "montage", "somnole", "travaux"], 
            "8" : ["javelot", "losange", "spirale", "aquarium", "brocante", "diapason","objectif", "logiciel", "pastiche", "scorpion", "tabouret", "triangle", "utopique", "cascade", "boussole", "tornades", "panthère", "mystique", "tournage", "lumières", "fracture", "barbecue", "grenoble", "volcanes", "clarté", "chaleurs", "bourgeon", "printemps", "moulinet", "sauvages", "parfume", "fenêtres", "riviere", "mosaïque", "frissons", "tonnerre", "brouhaha", "marathon", "symphony", "cloporte", "moissons", "cascadeur", "periscope"]
}


import tkinter as tk
import random as rd

def lettres3():
    mot=rd.choise(Listemots[3])
    return mot
def lettres4():
    mot=rd.choise(Listemots[3])
    return mot
def lettres5():
    mot=rd.choise(Listemots[3])
    return mot
def lettres6():
    mot=rd.choise(Listemots[3])
    return mot
def lettres7():
    mot=rd.choise(Listemots[3])
    return mot
def lettres8():
    mot=rd.choise(Listemots[3])
    return mot


racine=tk.Tk()

choisir_longueur=tk.Label(racine, "cliquez sur la longueur du mot")
choisir_longueur.grid(column=0,row=1, padx=10, pady=10)

bouton1=tk.Button(racine, "3 lettres", command=lettres3)
bouton2=tk.Button(racine, "4 lettres", command=lettres4)
bouton3=tk.Button(racine, "5 lettres", command=lettres5)
bouton4=tk.Button(racine, "6 lettres", command=lettres6)
bouton5=tk.Button(racine, "7 lettres", command=lettres7)
bouton6=tk.Button(racine, "8 lettres", command=lettres8)

bouton1.grid()
bouton2.grid()
bouton3.grid()
bouton4.grid()
bouton5.grid()
bouton6.grid()
