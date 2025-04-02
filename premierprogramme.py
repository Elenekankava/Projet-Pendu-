
import tkinter as tk

racine= tk.Tk()
racine.title("jeu du pendu")
racine.geometry("800x600")

def clear_window():
    for widget in racine.winfo_children():
        widget.destroy()

def page_intruction():
    clear_window
    textes=tk.Label(racine, text='instructions', font='30', fg='black')
    textes.grid()

def deuxieme_page():
    clear_window

def premiere_page():
    canvas=tk.Canvas(racine, width=500, height=500)
    canvas.grid()
    texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue")
    texte.grid(column=0, row=0, padx=10, pady=10)


boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black")
boutoninstructions.grid(column=0, row=1, padx=10, pady=10)
boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black")
boutondebutjeu.grid(column=0, row=2, padx=10, pady=10)

premiere_page()

racine.mainloop()