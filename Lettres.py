import tkinter as tk
racine=tk.Tk()

def affichage(bouton)->None:
    """affiche la lettre sur le bouton"""
    bouton.config(bg='black',fg='black')
    global lettre
    lettre=str(bouton)
    if len(lettre)==9:
        numero=(lettre[8])
    elif len(lettre)==10:
        numero=(str(lettre[8])+str(lettre[9]))
    lettre = chr(int(numero) + 64)
    return lettre
    

bouton_a = tk.Button(racine,text='A',command=lambda : affichage(bouton_a), activebackground='black', foreground='blue')
bouton_a.grid(column=0, row=0)

bouton_b = tk.Button(racine,text='B',command=lambda : affichage(bouton_b), activebackground='black', foreground='blue')
bouton_b.grid(column=1, row=0)

bouton_c = tk.Button(racine,text='C',command=lambda : affichage(bouton_c), activebackground='black', foreground='blue')
bouton_c.grid(column=2, row=0)

bouton_d = tk.Button(racine,text='D',command=lambda : affichage(bouton_d), activebackground='black', foreground='blue')
bouton_d.grid(column=3, row=0)

bouton_e = tk.Button(racine,text='E',command=lambda : affichage(bouton_e), activebackground='black', foreground='blue')
bouton_e.grid(column=4, row=0)

bouton_f = tk.Button(racine,text='F',command=lambda : affichage(bouton_f), activebackground='black', foreground='blue')
bouton_f.grid(column=5, row=0)

bouton_g = tk.Button(racine,text='G',command=lambda : affichage(bouton_g), activebackground='black', foreground='blue')
bouton_g.grid(column=6, row=0)

bouton_h = tk.Button(racine,text='H',command=lambda : affichage(bouton_h), activebackground='black', foreground='blue')
bouton_h.grid(column=7, row=0)

bouton_i = tk.Button(racine,text='I',command=lambda : affichage(bouton_i), activebackground='black', foreground='blue')
bouton_i.grid(column=8, row=0)

bouton_j = tk.Button(racine,text='J',command=lambda : affichage(bouton_j), activebackground='black', foreground='blue')
bouton_j.grid(column=9, row=0)

bouton_k = tk.Button(racine,text='K',command=lambda : affichage(bouton_k), activebackground='black', foreground='blue')
bouton_k.grid(column=10, row=0)

bouton_l = tk.Button(racine,text='L',command=lambda : affichage(bouton_l), activebackground='black', foreground='blue')
bouton_l.grid(column=11, row=0)

bouton_m = tk.Button(racine,text='M',command=lambda : affichage(bouton_m), activebackground='black', foreground='blue')
bouton_m.grid(column=12, row=0)

bouton_n = tk.Button(racine,text='N',command=lambda : affichage(bouton_n), activebackground='black', foreground='blue')
bouton_n.grid(column=0, row=1)

bouton_o = tk.Button(racine,text='O',command=lambda : affichage(bouton_o), activebackground='black', foreground='blue')
bouton_o.grid(column=1, row=1)

bouton_p = tk.Button(racine,text='P',command=lambda : affichage(bouton_p), activebackground='black', foreground='blue')
bouton_p.grid(column=2, row=1)

bouton_q = tk.Button(racine,text='Q',command=lambda : affichage(bouton_q), activebackground='black', foreground='blue')
bouton_q.grid(column=3, row=1)

bouton_r = tk.Button(racine,text='R',command=lambda : affichage(bouton_r), activebackground='black', foreground='blue')
bouton_r.grid(column=4, row=1)

bouton_s = tk.Button(racine,text='S',command=lambda : affichage(bouton_s), activebackground='black', foreground='blue')
bouton_s.grid(column=5, row=1)

bouton_t = tk.Button(racine,text='T',command=lambda : affichage(bouton_t), activebackground='black', foreground='blue')
bouton_t.grid(column=6, row=1)

bouton_u = tk.Button(racine,text='U',command=lambda : affichage(bouton_u), activebackground='black', foreground='blue')
bouton_u.grid(column=7, row=1)

bouton_v = tk.Button(racine,text='V',command=lambda : affichage(bouton_v), activebackground='black', foreground='blue')
bouton_v.grid(column=8, row=1)

bouton_w= tk.Button(racine,text='W',command=lambda : affichage(bouton_w), activebackground='black', foreground='blue')
bouton_w.grid(column=9, row=1)

bouton_x = tk.Button(racine,text='X',command=lambda : affichage(bouton_x), activebackground='black', foreground='blue')
bouton_x.grid(column=10, row=1)

bouton_y = tk.Button(racine,text='Y',command=lambda : affichage(bouton_y), activebackground='black', foreground='blue')
bouton_y.grid(column=11, row=1)

bouton_z = tk.Button(racine,text='Z',command=lambda : affichage(bouton_z), activebackground='black', foreground='blue')
bouton_z.grid(column=12, row=1)

racine.mainloop()