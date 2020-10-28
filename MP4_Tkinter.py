import sqlite3
from tkinter import * 
from tkinter.ttk import * 

#---------------------------------------------------------------------------------------------------------------------------  

def choix1():
    global choix
    quitter()
    choix = 1

def choix2():
    global choix
    quitter()
    choix = 2
    
def choix3():
    global choix
    quitter()
    choix = 3

def choix4():
    global choix
    quitter()
    choix = 4

def Exit():
    global choix
    fenetre.destroy()
    fenetre.quit()
    choix = 5
    
def quitter():
    fenetre.destroy()
    fenetre.quit()

def conectBDD():
    conn = sqlite3.connect('Annuaire.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS ANNUAIRE
                    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TECT, tel INT,
                    email TEXT, qualité TEXT)""")
  
def ajouterBDD():
    
    datas = nom.get() , prenom.get() , tel.get() , email.get() , qualité.get()
    
    cur.execute("INSERT INTO ANNUAIRE(nom,prenom,tel,email,qualité) VALUES(?, ?, ?, ?, ?)" , datas)
    conn.commit()
    
    fenetre.destroy()
    fenetre.quit()

def suprBDD():
    
    cur.execute('SELECT * FROM ANNUAIRE')
    conn.commit()
    BD = cur.fetchall()        
    
    nom = BD[int(supr.get())-1][1]
    prenom = BD[int(supr.get())-1][2]
    
    suppr = (nom,prenom)
        
    cur.execute('DELETE FROM ANNUAIRE WHERE nom = ? AND prenom = ?', suppr)
    conn.commit()
    
    fenetre.destroy()
    fenetre.quit()

def modifBDD(colone, colone_connu, ligne, modif) :

    modif = (modif, ligne)
    
    cur.execute('UPDATE ANNUAIRE SET {} = ? WHERE {} = ?'.format(colone, colone_connu), modif)
    conn.commit()

def rechBDD(colone, colone_cond, ligne_cond, cond):
    
    if cond == "oui":
        ligne_cond = (ligne_cond,)
        cur.execute('SELECT {} FROM ANNUAIRE WHERE {} = ?'.format(colone, colone_cond), (ligne_cond))
    else:
        cur.execute('SELECT {} FROM ANNUAIRE'.format(colone))
    conn.commit()
    print('\n',cur.fetchall())


conn = sqlite3.connect('Annuaire.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ANNUAIRE
                (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TECT, tel INT,
                email TEXT, qualité TEXT)""")

fenetre = Tk()

Button(fenetre, text="AJOUT", command=choix1).pack(pady = 5)
Button(fenetre, text="SUPRESSION", command=choix2).pack(pady = 5)
Button(fenetre, text="MODIFICATION", command=choix3).pack(pady = 5)
Button(fenetre, text="BDD", command=choix4).pack(pady = 5)
Button(fenetre, text="EXIT", command=Exit).pack(pady = 5)

fenetre.mainloop()
while choix != 5:
    if choix == 1:
       
        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit).pack(side = TOP, fill = X, pady = 5)

        Label(fenetre, text= 'Ajout dans la base de donnée').pack(side=TOP, pady=10)
        
        Label(fenetre, text = 'Nom (string) :').pack(side=TOP, padx=5, pady=5)
        nom = Entry(fenetre, width=30)
        nom.pack(side = TOP,padx=5, pady=5)
        
        Label(fenetre, text = 'Prénom (string) :').pack(side=TOP, padx=5, pady=5)
        prenom = Entry(fenetre, width=30)
        prenom.pack(side = TOP,padx=5, pady=5)
                
        Label(fenetre, text = 'Tel (int) :').pack(side=TOP, padx=5, pady=5)
        tel = Entry(fenetre, width=30)
        tel.pack(side = TOP,padx=5, pady=5)
        
        Label(fenetre, text = 'Email (string) :').pack(side=TOP, padx=5, pady=5)
        email = Entry(fenetre, width=30)
        email.pack(side = TOP,padx=5, pady=5)
                
        Label(fenetre, text = 'Qualité (string) :').pack(side=TOP, padx=5, pady=5)
        qualité = Entry(fenetre, width=30)
        qualité.pack(side = TOP,padx=5, pady=5)        
        
        Button(fenetre, text="Fermer", command=quitter).pack(side = BOTTOM, padx=5, pady=5)
        Button(fenetre, text='Ajouter', command=ajouterBDD).pack(side = BOTTOM, padx=5, pady=5)       
        
        fenetre.mainloop()


    elif choix == 2:
        
        ID = []

        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit).pack(side = TOP, fill = X, pady = 5)
        
        tableau = Treeview(fenetre, columns=('ID', 'NOM', 'PRENOM', 'TELEPHONE', 'EMAIL', 'QUALITE'))
        tableau.heading('ID', text='ID')
        tableau.heading('NOM', text='NOM')
        tableau.heading('PRENOM', text='PRENOM')
        tableau.heading('TELEPHONE', text='TELEPHONE')
        tableau.heading('EMAIL', text='EMAIL')
        tableau.heading('QUALITE', text='QUALITE')
        tableau['show'] = 'headings' 
        tableau.pack(padx = 5, pady = (0, 5))
        
        for i in range(len(BD)):
            tableau.insert('', 'end', iid=i, values=(i+1, BD[i][1], BD[i][2], BD[i][3], BD[i][4], BD[i][5]))
            ID.append(i+1)
        
        Label(fenetre, text= 'Que suprimer (ID) ?').pack(pady=5)

        supr = Combobox(fenetre, values=ID)
        supr.current(0)
        supr.pack()
        
        Button(fenetre, text="Suprimer", command=suprBDD).pack()
        
        Button(fenetre, text="Fermer", command=quitter).pack()
               
        fenetre.mainloop()        

    elif choix == 3:
        colone = input("Quelle colone modifier ?\n"
                        "(nom, prenom, tel ,email, qualité)\n")
        colone_connu = input("De quelle colone est la donnée connue ?\n"
                      "(nom, prenom, tel ,email, qualité)\n")
        ligne = input("Quelle est la donnée connu de {} ?\n".format(colone_connu))
        modif = input("Avec quelle donnée changer {} ? \n".format(colone))
        modifBDD(colone, colone_connu, ligne, modif)        

    elif choix == 4:

        cur.execute('SELECT * FROM ANNUAIRE')
        conn.commit()
        BD = cur.fetchall()
        print(BD)


        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit).pack(side = TOP, fill = X, pady = 5)

        tableau = Treeview(fenetre, columns=('NOM', 'PRENOM', 'TELEPHONE', 'EMAIL', 'QUALITE'))
        tableau.heading('NOM', text='NOM')
        tableau.heading('PRENOM', text='PRENOM')
        tableau.heading('TELEPHONE', text='TELEPHONE')
        tableau.heading('EMAIL', text='EMAIL')
        tableau.heading('QUALITE', text='QUALITE')
        tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
        tableau.pack(padx = 5, pady = (0, 5))
        
        for i in range(len(BD)):
            tableau.insert('', 'end', iid=i+1, values=(BD[i][1], BD[i][2], BD[i][3], BD[i][4], BD[i][5]))
        
        bouton=Button(fenetre, text="Fermer", command=quitter).pack()

        fenetre.mainloop()
        
    if choix != 5:          
        fenetre = Tk()

        Button(fenetre, text="AJOUT", command=choix1).pack(pady = 5)
        Button(fenetre, text="SUPRESSION", command=choix2).pack(pady = 5)
        Button(fenetre, text="MODIFICATION", command=choix3).pack(pady = 5)
        Button(fenetre, text="BDD", command=choix4).pack(pady = 5)
        Button(fenetre, text="EXIT", command=Exit).pack(pady = 5)
        
        fenetre.mainloop() 
       

cur.close()
conn.close()
print("\nFin du programme")