
import tkinter as tk

def show_instructions():
    window=tk.Toplevel(racine)

racine= tk.Tk()
racine.title("jeu du pendu")


boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black")
boutoninstructions.grid(column=0, row=1, padx=10, pady=10)

def demarrer():
    texte.destroy()
    boutoninstructions.destroy()
    global t
    t=True

canvas=tk.Canvas(racine, width=500, height=500)
canvas.grid()

texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue")
texte.grid(column=0, row=0, padx=10, pady=10)



boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black", command=demarrer())
boutondebutjeu.grid(column=0, row=2, padx=10, pady=10)

if t==True:
    boutondebutjeu.destroy()


racine.mainloop()