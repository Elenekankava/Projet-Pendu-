
import tkinter as tk

racine= tk.Tk()
racine.title("jeu du pendu")

def show_instructions():
    window=tk.Toplevel(racine)

def demarrer():
    texte.destroy()
    boutondebutjeu.destroy()
    boutoninstructions.destroy()
    
canvas=tk.Canvas(racine, width=500, height=500)
canvas.grid()

texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue")
texte.grid(column=0, row=0, padx=10, pady=10)

boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black", command = show_instructions())
boutoninstructions.grid(column=0, row=1, padx=10, pady=10)

boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black", command=demarrer())
boutondebutjeu.grid(column=0, row=2, padx=10, pady=10)




racine.mainloop()