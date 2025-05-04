import tkinter as tk
from functools import partial
import random as rd
import itertools

racine= tk.Tk()
racine.title("jeu du pendu")
racine.geometry("800x800")

#Listemots= {"3": ["coq", "ski", "jus", "nul","gaz", "axe", "rat", "feu", "mur", "sel", "bot", "tas", "lot", "jeu", "lac", "bol", "nid", "par", "riz", "mot", "vue", "but", "ton", "fin", "mer", "air", "sol", "don", "bar", "vue", "pis", "roc", "vie", "fer", "cap", "ron"],
            #"4": ["beau", "joli", "thym", "yogi", "pion", "chat", "loup", "noir", "vert", "bleu", "port", "tour", "mont", "lait", "pain", "robe", "bain", "vent", "camp", "sole", "gris", "bois", "ciel", "dent", "faux", "rose", "pont", "doux", "cord", "film", "main", "pois", "vide", "clou", "fort"],
            #"5" : ["bruit", "cycle", "livre", "pomme", "tenue", "rugby", "table", "plage", "valse", "ferme", "ombre", "sable", "chute", "glace", "fleur", "porte", "verre", "moulin", "colis", "grille", "dalle", "piano", "tronc", "danse", "carte", "farce", "goule", "louve", "plain", "coeur", "train", "flute", "morce", "signe", "tigre", "phase"],
            #"6" : ["agneau", "alarme", "ananas", "arcade", "billet", "garage", "oiseau", "pierre", "valise", "tunnel", "fusain", "marais", "chemin", "barque", "forger", "cloche", "rapide", "soleil", "frambo", "gouter", "danser", "ranger", "fossil", "plante", "crayon", "bourse", "lamper", "bassin", "piston", "moulin", "courir", "lancer", "tordre", "filmer", "bercer", "manger", "chalet"],
            #"7" : ["puzzle", "abriter", "billard", "chariot", "crapaud", "fourmis", "iceberg", "valence", "clocher", "brasier", "lantern", "tranche", "pendule", "grenade", "cheveux", "voltage", "moteurs", "fenetre", "gourdin", "drapier", "saboter", "mystère", "plafond", "rempart", "baroque", "cascade", "lumiere", "bousier", "tresser", "marguer", "torrent", "siffler", "gravure", "palabre", "montage", "somnole", "travaux"], 
            #"8" : ["javelot", "losange", "spirale", "aquarium", "brocante", "diapason","objectif", "logiciel", "pastiche", "scorpion", "tabouret", "triangle", "utopique", "cascade", "boussole", "tornades", "panthère", "mystique", "tournage", "lumières", "fracture", "barbecue", "grenoble", "volcanes", "clarté", "chaleurs", "bourgeon", "printemps", "moulinet", "sauvages", "parfume", "fenêtres", "riviere", "mosaïque", "frissons", "tonnerre", "brouhaha", "marathon", "symphony", "cloporte", "moissons", "cascadeur", "periscope"]
#}

Listemots= {"3":
    {"coq": "Chante au lever du jour",
    "ski": "Glisse sur la neige",
    "jus": "Boisson de fruit",
    "nul": "Sans valeur",
    "gaz": "État de la matière",
    "axe": "Ligne de rotation",
    "rat": "Rongeur urbain",
    "feu": "Produit de la combustion",
    "mur": "Séparation verticale",
    "sel": "Assaisonne les plats",
    "bot": "Automate informatique",
    "tas": "Petit amas",
    "lot": "Gagné à une tombola",
    "jeu": "Activité ludique",
    "lac": "Étendue d’eau douce",
    "bol": "Contenant pour soupe",
    "nid": "Maison d’oiseau",
    "par": "Préposition de passage",
    "riz": "Céréale asiatique",
    "mot": "Unité de langage",
    "vue": "Sens des yeux",
    "but": "Objectif atteint",
    "ton": "Variation de voix",
    "fin": "Opposé de début",
    "mer": "Grande étendue salée",
    "air": "Mélange de gaz",
    "sol": "Surface de la Terre",
    "don": "Cadeau désintéressé",
    "bar": "Lieu pour boire",
    "pis": "Pire ou mamelle",
    "roc": "Gros rocher",
    "vie": "Opposé de mort",
    "fer": "Métal magnétique",
    "cap": "Direction à suivre",
    "ron": "Début de “ronron”"},
    "4": 
    {"beau": "Agréable à regarder",
    "joli": "Charmant ou mignon",
    "thym": "Plante aromatique",
    "yogi": "Pratique le yoga",
    "pion": "Pièce d’échec",
    "chat": "Félin domestique",
    "loup": "Prédateur en meute",
    "noir": "Absence de couleur",
    "vert": "Couleur de l’herbe",
    "bleu": "Couleur du ciel",
    "port": "Où accostent les bateaux",
    "tour": "Édifice ou rotation",
    "mont": "Hauteur naturelle",
    "lait": "Boisson blanche",
    "pain": "Fait avec de la farine",
    "robe": "Vêtement féminin",
    "bain": "Prendre dans une baignoire",
    "vent": "Air en mouvement",
    "camp": "Lieu temporaire de repos",
    "sole": "Poisson plat",
    "gris": "Couleur nuageuse",
    "bois": "Matériau des arbres",
    "ciel": "Au-dessus de nos têtes",
    "dent": "Dans la bouche",
    "faux": "Pas vrai",
    "rose": "Fleur ou couleur",
    "pont": "Permet de traverser",
    "doux": "Agréable au toucher",
    "cord": "Synonyme de corde",
    "film": "Projeté au cinéma",
    "main": "Au bout du bras",
    "pois": "Légume rond",
    "vide": "Sans contenu",
    "clou": "Fixe dans le bois",
    "fort": "Plein de force"},
    "5" : 
    {"bruit": "Son fort ou désagréable",
    "cycle": "Suite qui recommence",
    "livre": "À lire",
    "pomme": "Fruit défendu",
    "tenue": "Vêtement complet",
    "rugby": "Sport avec un ballon ovale",
    "table": "Meuble de repas",
    "plage": "Sable au bord de mer",
    "valse": "Danse à trois temps",
    "ferme": "Exploit. agricole",
    "ombre": "Zone sans lumière",
    "sable": "Grains sur la plage",
    "chute": "Perte d’équilibre",
    "glace": "Eau gelée ou dessert",
    "fleur": "Plante colorée",
    "porte": "S’ouvre et se ferme",
    "verre": "Matériau transparent",
    "moulin": "Tour qui broie",
    "colis": "Objet à livrer",
    "grille": "Treillis métallique",
    "dalle": "Plaque de sol",
    "piano": "Instrument à touches",
    "tronc": "Partie centrale de l’arbre",
    "danse": "Mouvement rythmé",
    "carte": "Représentation géographique",
    "farce": "Blague ou garniture",
    "goule": "Créature monstrueuse",
    "louve": "Femelle du loup",
    "plain": "Synonyme de plaine",
    "coeur": "Organe ou amour",
    "train": "Moyen de transport ferré",
    "flute": "Instrument à vent",
    "morce": "Petit bout",
    "signe": "Geste ou symbole",
    "tigre": "Félin rayé",
    "phase": "Étape d’un cycle"},
    "6" : 
    {"agneau": "Petit mouton",
    "alarme": "Alerte sonore",
    "ananas": "Fruit tropical",
    "arcade": "Voûte ou salle de jeux",
    "billet": "Pour voyager ou entrer",
    "garage": "Abri pour voiture",
    "oiseau": "Animal volant",
    "pierre": "Morceau de roche",
    "valise": "Contenant de voyage",
    "tunnel": "Galerie souterraine",
    "fusain": "Crayon d’artiste",
    "marais": "Zone marécageuse",
    "chemin": "Sentier ou route",
    "barque": "Petit bateau",
    "forger": "Travailler le métal",
    "cloche": "Fait “ding dong”",
    "rapide": "Très vite",
    "soleil": "Astro qui éclaire",
    "frambo": "Début de fruit rouge",
    "gouter": "Manger un peu",
    "danser": "Bouger en rythme",
    "ranger": "Mettre en ordre",
    "fossil": "Trace d’être vivant ancien",
    "plante": "Organisme vert",
    "crayon": "Pour écrire ou dessiner",
    "bourse": "Marché financier",
    "lamper": "Boire d’un trait",
    "bassin": "Petit plan d’eau",
    "piston": "Pièce de moteur",
    "moulin": "Broie ou tourne au vent",
    "courir": "Aller vite à pied",
    "lancer": "Projeter avec force",
    "tordre": "Déformer en tournant",
    "filmer": "Enregistrer en vidéo",
    "bercer": "Calmer un bébé",
    "manger": "Nourrir son ventre",
    "chalet": "Maison de montagne"},
    "7" : 
    {"puzzle": "Jeu d’assemblage",
    "abriter": "Mettre à l’abri",
    "billard": "Jeu de boules",
    "chariot": "Pour transporter des charges",
    "crapaud": "Amphibien verruqueux",
    "fourmis": "Petits insectes en colonie",
    "iceberg": "Grosse glace flottante",
    "valence": "Ville ou chimie",
    "clocher": "Tour d’église",
    "brasier": "Feu intense",
    "lantern": "Éclaire la nuit",
    "tranche": "Morceau coupé fin",
    "pendule": "Horloge murale",
    "grenade": "Fruit ou explosif",
    "cheveux": "Sur la tête",
    "voltage": "Tension électrique",
    "moteurs": "Font avancer machines",
    "fenetre": "Ouverture dans un mur",
    "gourdin": "Bâton épais",
    "drapier": "Vendeur de tissus",
    "saboter": "Détruire discrètement",
    "mystère": "Chose inconnue",
    "plafond": "Haut d’une pièce",
    "rempart": "Mur de défense",
    "baroque": "Style artistique chargé",
    "cascade": "Chute d’eau",
    "lumiere": "Éclaire l’obscurité",
    "bousier": "Insecte rouleur de bouse",
    "tresser": "Faire des tresses",
    "marguer": "Début de fleur blanche",
    "torrent": "Rivière rapide",
    "siffler": "Faire un son aigu",
    "gravure": "Image gravée",
    "palabre": "Longue discussion",
    "montage": "Assemblage d’éléments",
    "somnole": "Dort à moitié",
    "travaux": "Chantiers ou devoirs"}, 
    "8" : 
    {"javelot": "Lancé aux Jeux Olympiques",
    "losange": "Figure géométrique",
    "spirale": "Forme tournante",
    "aquarium": "Maison à poissons",
    "brocante": "Marché d’objets anciens",
    "diapason": "Donne la note LA",
    "objectif": "But à atteindre",
    "logiciel": "Programme informatique",
    "pastiche": "Imitation artistique",
    "scorpion": "Animal à pinces et dard",
    "tabouret": "Siège sans dossier",
    "triangle": "Trois côtés",
    "utopique": "Idéal irréaliste",
    "cascade": "Chute d’eau (encore !)",
    "boussole": "Indique le nord",
    "tornades": "Violente tempête tournante",
    "panthère": "Félin tacheté ou noir",
    "mystique": "Spirituel ou mystérieux",
    "tournage": "Réalisation de film",
    "lumières": "Ce qui éclaire",
    "fracture": "Os cassé",
    "barbecue": "Cuisine au charbon",
    "grenoble": "Ville des Alpes",
    "volcanes": "Montagnes explosives",
    "clarté": "Lumière ou compréhension",
    "chaleurs": "Temps très chaud",
    "bourgeon": "Futur feuille ou fleur",
    "printemps": "Saison après l’hiver",
    "moulinet": "Pour remonter la ligne",
    "sauvages": "Pas domestiqués",
    "parfume": "Donne une bonne odeur",
    "fenêtres": "Ouvertures vitrées",
    "riviere": "Cours d’eau doux",
    "mosaïque": "Image en petits morceaux",
    "frissons": "Sensation de froid ou peur",
    "tonnerre": "Suit l’éclair",
    "brouhaha": "Grand bruit confus",
    "marathon": "Course de 42 km",
    "symphony": "Grande œuvre musicale",
    "cloporte": "Petit insecte gris",
    "moissons": "Récolte des céréales",
    "cascadeur": "Double pour scènes risquées",
    "periscope": "Voir sans être vu"}
}
cpt = 0
ecriture_score=' '
global lettre_deja_dite
lettre_deja_dite=[]
global numero_partie
numero_partie=0
print(lettre_deja_dite)
apparition_page_trois=0

def show_selection(choices, listbox):
    choices = choices.get()
    selection = listbox.curselection()
    if not selection:
        return
    taille = listbox.get(selection[0])
    global mot
    global indication
    print(taille)
    variable = Listemots[str(taille)]
    items=[(sk, v) for sk, v in variable.items()]
    random_item = rd.choice(items)
    mot=random_item[0]
    indication=random_item[1]
    mot=str(mot)
    global text
    text=len(mot)
    print(mot)
    print(indication)
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
    
    

def apparition_lettre(event):
    """affiche la lettre sur le bouton"""
    message.config(text='')
    c=0
    lettre=str(event.char)
    print(lettre)
    global ecriture_score
    global numero_partie
    global cpt
    global lettre_deja_dite
    global apparition_page_trois
    global ecriture
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
            fin_demande_rejouer()
            numero_partie+=1
            apparition_page_trois=0
    if affichage == list(mot):
        numero_partie+=1
        score=cpt
        ecriture_score=str(ecriture_score)+'\n'+'score de la parite numero '+str(numero_partie)+' : '+str(score)
        lettre_deja_dite=[]
        cpt=0
        apparition_page_trois=0
        page_victoire()   


x0= 600
y= 100
x1= 850
y1= 155
def dessin_etape1():
    ligne1_etape1= canvas.create_line(x0, y, x1, y)
    ligne2_etape1=canvas.create_line(x0, y, x0, y + 300)
    ligne3_etape1=canvas.create_line(x0-10, y, x0 + 100,y)
    ligne4_etape1= canvas.create_line(x1, y, x1, y +30)
    ligne_diagonale_etape1= canvas.create_line(x0 + 20, y, x0, y+ 20)
    ligne_horizontale_etape1= canvas.create_line(x0- 10, y+ 300, x1-150, y+300)

def dessin_etape2():
    dessin_etape1()
    cercle= canvas.create_oval((x1 - 25, y1+ 25), (x1 + 25, y1- 25), width=3, fill="misty rose")
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
    canvas= tk.Canvas(racine,width= 1000, height=800,bg='lavender')
    canvas.grid()
    cercle=canvas.create_oval((800-75, 250-75),(800+75, 250+75), fill="black")
    cercle=canvas.create_oval((800-70, 250-70),(800+70, 250+70), fill="misty rose")
    yeux1=canvas.create_oval((770-15, 230-15),(770+15, 230+15), fill="black")
    yeux2=canvas.create_oval((830-15, 230-15),(830+15, 230+15), fill="black")
    bouche=canvas.create_line((770,280),(820,280), fill="black", width=4)

def asterix (word) :
    word_l=list(word)
    nombre_asterix=len(word_l)
    global affichage
    affichage = [' *  '] * len(word)
    ecriture=' '.join(affichage)
    texte.config(text=str(ecriture), fg='black', font=30)


def clear_window():
    for widget in racine.winfo_children():
        widget.destroy()

def page_aide() :
    clear_window()
    racine['bg'] = 'lavender'
    encadrertexte=tk.Frame(racine, bg="orchid4", bd=4, relief='solid')
    encadrertexte.place(x=200, y=150, width=900, height=500)
    textes=tk.Label(racine, text='Vous commencerez par sélectionner la longueur du mot que vous souhaitez deviner.\n Ensuite, le but est de deviner le mot générer par l’ordinateur \n avant que le dessin du pendu se termine.\n A chaque essaie vous proposerez une lettre, si elle est dans le mot la lettre s’affiche à l’écran,\n si elle ne l’est pas le dessin du pendu avance d’une étape.\n Vous avez le droit à 8 échecs le but est de deviner le mot complet \n avant que le dessin du pendu soit finalisé.', font=('Rockwell', '15'), bg='lavender', fg='darkorchid4')
    textes.place(x=225,y=300)
    titre=tk.Label(racine, text='Instructions:', font=('showcard gothic', '25'), fg='darkorchid4')
    titre.place(x=200, y=100)
    bouton_retour=tk.Button(text='retour', command=troisieme_fenetre,bg='lavender',fg='darkorchid4',bd=4)
    bouton_retour.place(x=650, y=500)

def page_score() :
    clear_window()
    global ecriture_score
    ecriture_score_bouton=tk.Label(racine,text=str(ecriture_score))
    ecriture_score_bouton.grid()  
    bouton_retour_page_trois=tk.Button(racine, text='retour',command=troisieme_fenetre)  
    bouton_retour_page_trois.grid()

def affichage_indication():
    global indication
    text_indication.config(text=str(indication))

def troisieme_fenetre ():
    clear_window()
    global apparition_page_trois
    global text_indication
    global ecriture
    apparition_page_trois+=1
    text_indication=tk.Label(racine, text='',fg='white',bg='mediumorchid1')
    text_indication.grid()
    bouton_score=tk.Button(racine, text='score', command=page_score,fg='white',bg='mediumorchid1',bd=2)
    bouton_score.grid()
    bouton_indication=tk.Button(text='indication ?', command=affichage_indication,fg='white',bg='mediumorchid1',bd=2)
    bouton_indication.grid()
    racine['bg'] = 'lavender'
    global canvas
    canvas= tk.Canvas(racine,width= 1000, height=800,bg='lavender')
    canvas.grid()
    global texte
    texte=tk.Label(racine, text='')
    centrage_texte()
    racine.bind("<KeyPress>", apparition_lettre)
    bouton_aide=tk.Button(text='aide', command=page_aide,fg='white',bg='mediumorchid1',bd=2)
    bouton_aide.place(x=775,y=550)
    bouton_quitter=tk.Button(text='quitter la partie', command=premiere_page,fg='white',bg='mediumorchid1',bd=2)
    bouton_quitter.place(x=745,y=500)
    global message
    message=tk.Label(racine, text='')
    message.place(x=630,y=650)
    if apparition_page_trois==1 :
        asterix(mot)
    else :
        texte.config(text=str(ecriture))
    if cpt==0:
        dessin_etape1()
    elif cpt==1:
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


def page_intruction():
    clear_window()
    racine['bg'] = 'lavender'
    encadrertexte=tk.Frame(racine, bg="orchid4", bd=4, relief='solid')
    encadrertexte.place(x=200, y=150, width=900, height=500)
    textes=tk.Label(racine, text='Vous commencerez par sélectionner la longueur du mot que vous souhaitez deviner.\n Ensuite, le but est de deviner le mot générer par l’ordinateur \n avant que le dessin du pendu se termine.\n A chaque essaie vous proposerez une lettre, si elle est dans le mot la lettre s’affiche à l’écran,\n si elle ne l’est pas le dessin du pendu avance d’une étape.\n Vous avez le droit à 8 échecs le but est de deviner le mot complet \n avant que le dessin du pendu soit finalisé.', font=('Rockwell', '15'), bg='lavender', fg="dark orchid4")
    textes.place(x=225,y=300)
    titre=tk.Label(racine, text='Instructions:', font=('showcard gothic', '25'), fg='dark orchid4')
    titre.place(x=200, y=100)
    bouton_retour=tk.Button(text='retour', command=premiere_page,bg='lavender',fg="dark orchid4",bd=4)
    bouton_retour.place(x=650, y=500)

def deuxieme_page_choix():
    clear_window()
    racine['bg'] = 'lavender'
    encadrement = tk.Frame(racine,bg="orchid4", bd=4, relief='solid')
    encadrement.place(x=510, y=215, width=500, height=300)
    label1=tk.Label(racine,text='nombre de lettres que vous voulez dans le mot', font=('showcard gothic','20'),bg='lavender',fg='dark orchid4')
    choices = tk.Variable(racine, ('3', '4', '5','6'))
    listbox = tk.Listbox(racine, listvariable=choices, selectmode="simple",fg= "dark orchid4", bg='lavender',bd=2)
    listbox.insert('end', '7', '8')
    button = tk.Button(racine, text='Ok', command=partial(show_selection, choices, listbox),fg='dark orchid4',bg='lavender',bd=3)
    label1.place(x=425,y=165)
    listbox.place(x=700,y=260)
    button.place(x=750,y=445)
    
def premiere_page():
    clear_window()
    racine['bg'] = 'lavender'
    canvas=tk.Canvas(racine, width=1000, height=700,bg='lavender',bd=0)
    canvas.grid()
    texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Rockwell extra bold", '40'), fg="dark slate blue")
    texte.place(x=325, y=100)
    encadrement=tk.Frame(racine, bg="orchid4", bd=4, relief='solid')
    encadrement.place(x=325, y=200, width=900, height=400)
    boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("showcard gothic", "20"), bg="lavender", fg="dark orchid4", command=page_intruction)
    boutoninstructions.place(x=350, y=300)
    boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("showcard gothic", "20"), bg="lavender", fg="dark orchid4",command=deuxieme_page_choix)
    boutondebutjeu.place(x=400, y=450)

def dernier_page_du_jeu():
    clear_window()
    labelfin=tk.Label(text='Dommage! On espere vous revoir une autre fois!', font=('showcard gothic','30'), fg='dark orchid4')
    labelfin.place(x=150,y=300)

def page_victoire():
    clear_window()
    racine['bg'] = 'lavender'
    encadrerboutons=tk.Frame(racine, bg='lavender', bd=4, relief='solid')
    encadrerboutons.place(x=700, y=300, width='200', height='300')
    labelgagne=tk.Label(racine, text='Vous avez gagné!\n Souhaitez vous rejouer?', font=('showcard gothic','35'),fg="dark orchid4")
    labeltext=tk.Label(racine, text="Comme les sages le disent, une victoire est bien, deux ou plus encore meilleure;)", font=('french script mt', '30'),fg='dark orchid3')
    labeltext.place(x=350, y=215)
    bouton_oui=tk.Button(racine,text='oui', font=('showcard gothic','30'), command=deuxieme_page_choix,fg='orchid4',bg='lavender',bd=2)
    bouton_non=tk.Button(racine,text='non', font=('showcard gothic','30'), command=dernier_page_du_jeu,fg='orchid4',bg='lavender',bd=2)
    labelgagne.place(x=480,y=100)
    bouton_oui.place(x=745,y=325)
    bouton_non.place(x=743,y=450)

def fin_demande_rejouer():
    clear_window()
    racine['bg'] = 'lavender'
    encadrerboutons=tk.Frame(racine, bg='orchid4', bd=4, relief='solid')
    encadrerboutons.place(x=700, y=300, width='200', height='275')
    labelperdu=tk.Label(racine, text='Vous avez malheureusement perdu la partie!\n Souhaitez vous retenter votre chance?', font=('showcard gothic','35'),fg="dark orchid4")
    labeltext=tk.Label(racine, text="Comme les sages le disent, qui ne tente rien n'a rien ;)", font=('french script mt', '40'),fg = 'dark orchid3')
    labeltext.place(x=350, y=215)
    bouton_oui=tk.Button(racine,text='oui', font=('showcard gothic','30'), command=deuxieme_page_choix,fg='orchid4',bg='lavender',bd=2)
    bouton_non=tk.Button(racine,text='non', font=('showcard gothic','30'), command=dernier_page_du_jeu,fg='orchid4',bg='lavender',bd=2)
    labelperdu.place(x=220,y=100)
    bouton_oui.place(x=745,y=325)
    bouton_non.place(x=743,y=450)



premiere_page()

racine.mainloop()