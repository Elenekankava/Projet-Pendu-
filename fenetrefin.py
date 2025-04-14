def fenetre_fin:
    label= tk.Label(racine,text= "Vous avez perdu! Voulez vous faire une nouvelle partie?", font=("helvetica", "30"))
    bouton_oui= tk.Boutton(racine, text= "Oui, je veux rejouer!", command= premiere_page, padx= 30, pady= 30)
    bouton_non= tk.Boutton(racine, text= "Non, j'arrête.", command= clear_window, padx= 30, pady=30)
    label.grid(row= 1, column= 1, columnspan= 3)
    bouton_oui.grid(row= 3, column= 1)
    bouton_non.grid(row= 3, column= 2)