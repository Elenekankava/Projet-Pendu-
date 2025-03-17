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
    return

def dessin_etape2():
    dessin_etape1()
    cercle= canvas.create_oval((x1 - 25, y1+ 25), (x1 + 25, y1- 25), width=3, fill="pink")
    return

def dessin_etape3():
    dessin_etape2()
    corps=canvas.create_line((x1,y1),(x1,y1+25+60), width=3)
    return

def dessin_etape4():
    dessin_etape3()
    maingauche=canvas.create_line((x1, y1+25+10), (x1-15,y1-5), width=3)
    return
    
def dessin_etape5():
    dessin_etape4()
    maindroite=canvas.create_line((x1,y1+25+10), (x1+15, y1-5), width=3)
    
def dessin_etape6():
    dessin_etape5()
    piedgauche=canvas.create_line((x1-10, y1+25+60+15), (x1+10, y1+25+60+15), width=3)

def dessin_etape8():
    canvas.delete("all")
    cercle=canvas.create_oval((250-75, 250-75),(250+75, 250+75), fill="black")
    cercle=canvas.create_oval((250-70, 250-70),(250+70, 250+70), fill="pink")
    yeux1=canvas.create_oval((220-15, 230-15),(220+15, 230+15), fill="black")
    yeux2=canvas.create_oval((280-15, 230-15),(280+15, 230+15), fill="black")
    bouche=canvas.create_line((220,280),(270,280), fill="black", width=4)
     
dessin_etape8()
canvas.grid(column= 1, row= 3, columnspan= 11, rowspan= 10)

racine.mainloop()
