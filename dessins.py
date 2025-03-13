import tkinter as tk

racine= tk.Tk()
canvas= tk.Canvas(racine,width= 500, height=500)

x0= 100
y= 100
x1= 350
ligne1_etape1= canvas.create_line(x0, y, x1, y)
ligne2_etape1=canvas.create_line(x0, y, x0, y + 300)
ligne3_etape1=canvas.create_line(x0-10, y, x0 + 100,y)
ligne4_etape1= canvas.create_line(x1, y, x1, y +30)
ligne_diagonale_etape1= canvas.create_line(x0 + 20, y, x0, y+ 20)
ligne_horizontale_etape1= canvas.create_line(x0- 10, y+ 300, x1-150, y+300)

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

def dessin_etape2():
    dessin_etape1()
    cercle= canvas.create_oval(x1 - 25, y1+ 25, x1 + 25, y1- 25)
    
    


    
canvas.grid(column= 1, row= 3, columnspan= 11, rowspan= 10)

racine.mainloop()
