
import tkinter as tk

racine= tk.Tk()
racine.title("jeu du pendu")
racine.geometry("800x800")

def clear_window():
    for widget in racine.winfo_children():
        widget.destroy()

def page_intruction():
    clear_window()
    textes=tk.Label(racine, text='instructions', font='30', fg='black')
    textes.grid()
    bouton_retour=tk.Button

def deuxieme_page():
    clear_window()

def premiere_page():
    canvas=tk.Canvas(racine, width=500, height=500)
    canvas.grid()
    texte=tk.Label (racine, text="Bienvenue au Jeu du pendu!", font=("Helvetica", "40"),  fg="blue")
    texte.place(x=400, y=100)
    boutoninstructions=tk.Button (racine, text="Cliquez sur ce bouton afin de lire les instructions du jeu", font=("Helvetica", "20"), bg="pink", fg="black", command=page_intruction)
    boutoninstructions.place(x=370, y=500)
    boutondebutjeu= tk.Button(racine, text="Cliquez sur ce bouton afin de commencer a jouer", font=("Helvetica", "20"), bg="pink", fg="black",command=deuxieme_page)
    boutondebutjeu.place(x=400, y=700)


premiere_page()

racine.mainloop()