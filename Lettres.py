import tkinter as tk
racine=tk.Tk()

def affichage():
    """affiche la lettre sur le bouton"""
    global lettre
    label= tk.Label(racine, text=lettre,)

bouton_a = tk.Button(racine,text='A',command=affichage)
bouton_a.grid(column=0, row=0)

bouton_b = tk.Button(racine,text='B',command=affichage)
bouton_b.grid(column=1, row=0)

bouton_c = tk.Button(racine,text='C',command=affichage)
bouton_c.grid(column=2, row=0)

bouton_d = tk.Button(racine,text='D',command=affichage)
bouton_d.grid(column=3, row=0)

bouton_e = tk.Button(racine,text='E',command=affichage)
bouton_e.grid(column=4, row=0)

bouton_f = tk.Button(racine,text='F',command=affichage)
bouton_f.grid(column=5, row=0)

bouton_g = tk.Button(racine,text='G',command=affichage)
bouton_g.grid(column=6, row=0)

bouton_h = tk.Button(racine,text='H',command=affichage)
bouton_h.grid(column=7, row=0)

bouton_i = tk.Button(racine,text='I',command=affichage)
bouton_i.grid(column=8, row=0)

bouton_j = tk.Button(racine,text='J',command=affichage)
bouton_j.grid(column=9, row=0)

bouton_k = tk.Button(racine,text='K',command=affichage)
bouton_k.grid(column=10, row=0)

bouton_l = tk.Button(racine,text='L',command=affichage)
bouton_l.grid(column=11, row=0)

bouton_m = tk.Button(racine,text='M',command=affichage)
bouton_m.grid(column=12, row=0)

bouton_n = tk.Button(racine,text='N',command=affichage)
bouton_n.grid(column=0, row=1)

bouton_o = tk.Button(racine,text='O',command=affichage)
bouton_o.grid(column=1, row=1)

bouton_p = tk.Button(racine,text='P',command=affichage)
bouton_p.grid(column=2, row=1)

bouton_q = tk.Button(racine,text='Q',command=affichage)
bouton_q.grid(column=3, row=1)

bouton_r = tk.Button(racine,text='R',command=affichage)
bouton_r.grid(column=4, row=1)

bouton_s = tk.Button(racine,text='S',command=affichage)
bouton_s.grid(column=5, row=1)

bouton_t = tk.Button(racine,text='T',command=affichage)
bouton_t.grid(column=6, row=1)

bouton_u = tk.Button(racine,text='U',command=affichage)
bouton_u.grid(column=7, row=1)

bouton_v = tk.Button(racine,text='V',command=affichage)
bouton_v.grid(column=8, row=1)

bouton_w= tk.Button(racine,text='W',command=affichage)
bouton_w.grid(column=9, row=1)

bouton_x = tk.Button(racine,text='X',command=affichage)
bouton_x.grid(column=10, row=1)

bouton_y = tk.Button(racine,text='Y',command=affichage)
bouton_y.grid(column=11, row=1)

bouton_z = tk.Button(racine,text='Z',command=affichage)
bouton_z.grid(column=12, row=1)

racine.mainloop()