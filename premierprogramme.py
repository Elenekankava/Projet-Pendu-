
import tkinter as tk
from functools import partial
import random as rd

racine= tk.Tk()
racine.title("jeu du pendu")
racine.geometry("800x800")

Listemots= {"3": ["coq", "ski", "jus", "nul","gaz", "axe", "rat", "feu", "mur", "sel", "bot", "tas", "lot", "jeu", "lac", "bol", "nid", "par", "riz", "mot", "vue", "but", "ton", "fin", "mer", "air", "sol", "don", "bar", "vue", "pis", "roc", "vie", "fer", "cap", "ron"],
            "4": ["beau", "joli", "thym", "yogi", "pion", "chat", "loup", "noir", "vert", "bleu", "port", "tour", "mont", "lait", "pain", "robe", "bain", "vent", "camp", "sole", "gris", "bois", "ciel", "dent", "faux", "rose", "pont", "doux", "cord", "film", "main", "pois", "vide", "clou", "fort"],
            "5" : ["bruit", "cycle", "livre", "pomme", "tenue", "rugby", "table", "plage", "valse", "ferme", "ombre", "sable", "chute", "glace", "fleur", "porte", "verre", "moulin", "colis", "grille", "dalle", "piano", "tronc", "danse", "carte", "farce", "goule", "louve", "plain", "coeur", "train", "flute", "morce", "signe", "tigre", "phase"],
            "6" : ["agneau", "alarme", "ananas", "arcade", "billet", "garage", "oiseau", "pierre", "valise", "tunnel", "fusain", "marais", "chemin", "barque", "forger", "cloche", "rapide", "soleil", "frambo", "gouter", "danser", "ranger", "fossil", "plante", "crayon", "bourse", "lamper", "bassin", "piston", "moulin", "courir", "lancer", "tordre", "filmer", "bercer", "manger", "chalet"],
            "7" : ["puzzle", "abriter", "billard", "chariot", "crapaud", "fourmis", "iceberg", "valence", "clocher", "brasier", "lantern", "tranche", "pendule", "grenade", "cheveux", "voltage", "moteurs", "fenetre", "gourdin", "drapier", "saboter", "mystère", "plafond", "rempart", "baroque", "cascade", "lumiere", "bousier", "tresser", "marguer", "torrent", "siffler", "gravure", "palabre", "montage", "somnole", "travaux"], 
            "8" : ["javelot", "losange", "spirale", "aquarium", "brocante", "diapason","objectif", "logiciel", "pastiche", "scorpion", "tabouret", "triangle", "utopique", "cascade", "boussole", "tornades", "panthère", "mystique", "tournage", "lumières", "fracture", "barbecue", "grenoble", "volcanes", "clarté", "chaleurs", "bourgeon", "printemps", "moulinet", "sauvages", "parfume", "fenêtres", "riviere", "mosaïque", "frissons", "tonnerre", "brouhaha", "marathon", "symphony", "cloporte", "moissons", "cascadeur", "periscope"]
}



x0= 100
y= 100
x1= 350
y1= 155
def dessin_etape1():
    ligne1_etape1= canvas.create_line(x0, y, x1, y)
    ligne2_etape1=canvas.create_line(x0, y, x0, y + 300)
    ligne3_etape1=canvas.create_line(x0-10, y, x0 + 100,y)
    ligne4_etape1= canvas.create_line(x1, y, x1, y +30)
    ligne_diagonale_etape1= canvas.create_line(x0 + 20, y, x0, y+ 20)
    ligne_horizontale_etape1= canvas.create_line(x0- 10, y+ 300, x1-150, y+300)
    return

def dessin_etape2():
    dessin_etape1()
    cercle= canvas.create_oval((x1 - 25, y1+ 25), (x1 + 25, y1- 25), width=3, fill="pink")
    return

def dessin_etape3():
    dessin_etape2()
    corps=canvas.create_line((x1,y1+25),(x1,y1+25+70), width=3)
    return

def dessin_etape4():
    dessin_etape3()
    maingauche=canvas.create_line((x1, y1+25+20), (x1-40,y1+ 10), width=3)
    return
    
def dessin_etape5():
    dessin_etape4()
    maindroite=canvas.create_line((x1,y1+25+20), (x1+40, y1+ 10), width=3)
    
def dessin_etape6():
    dessin_etape5()
    piedgauche=canvas.create_line((x1, y1+25+70), (x1-30, y1+25+70+40), width=3)
    return

def dessin_etape7():
    dessin_etape6()
    pieddroite=canvas.create_line((x1, y1+25+70), (x1+30, y1+25+70+40), width=3)
    return

def dessin_etape8(canvas):
    canvas.delete("all")
    cercle=canvas.create_oval((250-75, 250-75),(250+75, 250+75), fill="black")
    cercle=canvas.create_oval((250-70, 250-70),(250+70, 250+70), fill="pink")
    yeux1=canvas.create_oval((220-15, 230-15),(220+15, 230+15), fill="black")
    yeux2=canvas.create_oval((280-15, 230-15),(280+15, 230+15), fill="black")
    bouche=canvas.create_line((220,280),(270,280), fill="black", width=4)

def asterix (word) :
    word_l=list(word)
    nombre_asterix=len(word_l)
    affichage=' *  '*nombre_asterix
    texte.config(text=str(affichage), fg='black', font=30)


def clear_window():
    for widget in racine.winfo_children():
        widget.destroy()

def troisieme_fenetre ():
    clear_window()
    global canvas
    canvas= tk.Canvas(racine,width= 500, height=500)
    canvas.grid()
    global texte
    texte=tk.Label(racine, text='')
    texte.grid()
    asterix(mot)
    dessin_etape1()

    

def show_selection(choices, listbox):
    choices = choices.get()
    text=""
    for index in listbox.curselection():
        text += choices[index]
    global mot
    mot = rd.choice(Listemots[str(text)])
    print(mot)
    troisieme_fenetre()
    return text

def page_intruction():
    clear_window()
    textes=tk.Label(racine, text='instructions', font='30', fg='black')
    textes.grid()
    bouton_retour=tk.Button(text='retour', command=premiere_page)
    bouton_retour.grid()

def deuxieme_page_choix():
    clear_window()
    label1=tk.Label(racine,text='nombre de lettres que vous voulez dans le mot', font='20')
    choices = tk.Variable(racine, ('3', '4', '5','6'))
    listbox = tk.Listbox(racine, listvariable=choices, selectmode="simple")
    listbox.insert('end', '7', '8')
    button = tk.Button(racine, text='Ok', command=partial(show_selection, choices, listbox))
    label1.grid(column=0, row=0)
    listbox.grid(row=1, column=0)
    button.grid(row=2, column=0)
    

def premiere_page():
    clear_window()
    canvas=tk.Canvas(racine, width=500, height=500)
    canvas.grid()
    texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue")
    texte.place(x=400, y=100)
    boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black", command=page_intruction)
    boutoninstructions.place(x=370, y=500)
    boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black",command=deuxieme_page_choix)
    boutondebutjeu.place(x=400, y=700)


premiere_page()

racine.mainloop()