def affichage():
    """affiche la lettre sur le bouton"""
    global lettre
    label= tk.Label(racine, text=lettre,)
bouton_a = tk.Boutton(racine,text=A,command=affichage)