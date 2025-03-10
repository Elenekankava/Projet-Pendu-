import tkinter as tk

racine= tk.Tk()
canvas= tk.Canvas(racine,width= 500, height=500)

x0= 100
y= 100
x1= 400
ligne1_etape1= canvas.create_line(x0, y, x1, y)
ligne2_etape1=canvas.create_line(x0, y, x0, y- 400)
ligne3_etape1=canvas.create_line(x0-50, y, x0 + 100,y)
ligne4_etape1= canvas.create_line(x1, y, x1, y- 30)
ligne_diagonale_etape1= canvas.create_line(x0 + 20, y, x0, y- 20)


canvas.grid(column= 1, row= 3, columnspan= 11, rowspan= 10)

racine.mainloop()
