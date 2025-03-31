
import tkinter as tk

racine= tk.Tk()
racine.title("jeu du pendu")
racine.configure(bg='white')

canvas=tk.Canvas(racine, width=500, height=500, bg='white')
canvas.grid()

texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue", bg='white')
texte.grid(column=0, row=0, padx=10, pady=10)

boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black")
boutoninstructions.grid(column=0, row=1, padx=10, pady=10)

boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black")
boutondebutjeu.grid(column=0, row=2, padx=10, pady=10)

racine.mainloop()