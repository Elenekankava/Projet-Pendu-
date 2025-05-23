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

cpt = 0
lettre_deja_dite=[]
def show_selection(choices, listbox):
    choices = choices.get()
    global text
    text=""
    for index in listbox.curselection():
        text += choices[index]
    global mot
    mot = rd.choice(Listemots[str(text)])
    mot=str(mot)
    print(mot)
    troisieme_fenetre()
    return text

def centrage_texte():
    if str(text) == '3':
        texte.place(x=745,y=600)
    if str(text) == '4':
        texte.place(x=727,y=600)
    if str(text) == '5':
        texte.place(x=709,y=600)
    if str(text) == '6':
        texte.place(x=691,y=600)
    if str(text) == '7':
        texte.place(x=675,y=600)
    if str(text) == '8':
        texte.place(x=665,y=600)
    
    

def affichage(event):
    """affiche la lettre sur le bouton"""
    message.config(text='')
    c=0
    lettre=str(event.char)
    print(lettre)
    global cpt
    print(lettre_deja_dite)
    if lettre in lettre_deja_dite:
        message.config(text="Vous avez déjà saisi cette lettre! Veuillez en saisir une différente!")
        return
    lettre_deja_dite.append(lettre)
    if lettre in (list(mot)):
        for i in range (len(list(mot))):
            if lettre==(list(mot))[i] :
                affichage[i]=lettre
        ecriture=' '.join(affichage)
        texte.config(text=str(ecriture))           
    else :
        cpt += 1
        if cpt==1:
            dessin_etape2()
        elif cpt== 2:
            dessin_etape3()
        elif cpt== 3:
            dessin_etape4()
        elif cpt== 4:
            dessin_etape5()
        elif cpt== 5:
            dessin_etape6()
        elif cpt== 6:
            dessin_etape7()
        elif cpt== 7:
            dessin_etape8()
        elif cpt>= 8:
            fenetre_fin()


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
    global affichage
    affichage=[]
    for i in range (nombre_asterix):
        affichage.append(' *  ')
    ecriture=' '.join(affichage)
    texte.config(text=str(ecriture), fg='black', font=30)


def clear_window():
    for widget in racine.winfo_children():
        widget.destroy()

def page_aide() :
    clear_window()
    textes=tk.Label(racine, text='Instructions\n Vous commencerez par sélectionner la longueur du mot que vous souhaitez deviner.\n Ensuite, le but est de deviner le mot générer par l’ordinateur avant que le dessin du pendu se termine.\n A chaque essaie vous proposerez une lettre en la tapant sur votre clavier, si elle est dans le mot la lettre s’affiche à l’écran, si elle ne l’est pas le dessin du pendu avance d’une étape.\n Vous avez le droit à 8 échecs le but est de deviner le mot complet avant que le dessin du pendu soit finalisé.', font='30', fg='black')
    textes.grid()
    bouton_retour=tk.Button(text='retour', command=troisieme_fenetre)
    bouton_retour.grid()
    

def troisieme_fenetre ():
    clear_window()
    global canvas
    canvas= tk.Canvas(racine,width= 500, height=500)
    canvas.grid()
    global texte
    texte=tk.Label(racine, text='' )
    centrage_texte()
    racine.bind("<KeyPress>", affichage)
    bouton_aide=tk.Button(text='aide', command=page_aide)
    bouton_aide.place(x=775,y=550)
    bouton_quitter=tk.Button(text='quitter la partie', command=premiere_page)
    bouton_quitter.place(x=745,y=500)
    global message
    message=tk.Label(racine, text='')
    message.place(x=630,y=650)
    asterix(mot)
    dessin_etape1()

    


def page_intruction():
    clear_window()
    textes=tk.Label(racine, text='Instructions\n Vous commencerez par sélectionner la longueur du mot que vous souhaitez deviner.\n Ensuite, le but est de deviner le mot générer par l’ordinateur avant que le dessin du pendu se termine.\n A chaque essaie vous proposerez une lettre, si elle est dans le mot la lettre s’affiche à l’écran, si elle ne l’est pas le dessin du pendu avance d’une étape.\n Vous avez le droit à 8 échecs le but est de deviner le mot complet avant que le dessin du pendu soit finalisé.', font='70', fg='black')
    textes.place(x=110,y=325)
    bouton_retour=tk.Button(text='retour', command=premiere_page)
    bouton_retour.place(x=760,y=485)

def deuxieme_page_choix():
    clear_window()
    label1=tk.Label(racine,text='nombre de lettres que vous voulez dans le mot', font='20')
    choices = tk.Variable(racine, ('3', '4', '5','6'))
    listbox = tk.Listbox(racine, listvariable=choices, selectmode="simple")
    listbox.insert('end', '7', '8')
    button = tk.Button(racine, text='Ok', command=partial(show_selection, choices, listbox))
    label1.place(x=565,y=500)
    listbox.place(x=700,y=260)
    button.place(x=750,y=445)
    

def premiere_page():
    clear_window()
    canvas=tk.Canvas(racine, width=500, height=500)
    canvas.grid()
    texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue")
    texte.place(x=475, y=100)
    boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black", command=page_intruction)
    boutoninstructions.place(x=455, y=300)
    boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black",command=deuxieme_page_choix)
    boutondebutjeu.place(x=485, y=500)


premiere_page()

racine.mainloop()