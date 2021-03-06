import sqlite3
from tkinter import * 
from tkinter.ttk import * 

#---------------------------------------------------------------------------------------------------------------------------  

def menu():
    global fenetre
    fenetre = Tk()

    Button(fenetre, text="AJOUT", command=choix1).pack(pady = 5, fill = X)
    Button(fenetre, text="SUPRESSION", command=choix2).pack(pady = 5, fill = X)
    Button(fenetre, text="MODIFICATION", command=choix3).pack(pady = 5, fill = X)
    Button(fenetre, text="VISUALISATION", command=choix4).pack(pady = 5, fill = X)
    Button(fenetre, text="EXIT", command=Exit).pack(pady = 5, fill = X)
    
    fenetre.mainloop()

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
    global choix, fenetre
    quitter()
    choix = 4

def Exit():
    global choix, fenetre
    fenetre.destroy()
    fenetre.quit()
    choix = 5
    
def quitter():
    global fenetre
    fenetre.destroy()
    fenetre.quit()

def conectBDD():
    conn = sqlite3.connect('Annuaire.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS ANNUAIRE
                    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TECT, tel INT,
                    email TEXT, qualité TEXT)""")
    
def donneBD():
    global BD
    cur.execute('SELECT * FROM ANNUAIRE')
    conn.commit()
    BD = cur.fetchall()
    
def afficherBD():
    global BD
    tableau = Treeview(fenetre, columns=('ID', 'NOM', 'PRENOM', 'TELEPHONE', 'EMAIL', 'QUALITE'))
    tableau.heading('ID', text='ID')
    tableau.heading('NOM', text='NOM')
    tableau.heading('PRENOM', text='PRENOM')
    tableau.heading('TELEPHONE', text='TELEPHONE')
    tableau.heading('EMAIL', text='EMAIL')
    tableau.heading('QUALITE', text='QUALITE')
    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.pack(padx = 5, pady = (0, 5))
    
    for i in range(len(BD)):
        tableau.insert('', 'end', iid=i+1, values=(i+1, BD[i][1], BD[i][2], BD[i][3], BD[i][4], BD[i][5]))
  
def ajouterBDD():
    
    datas = nom.get() , prenom.get() , tel.get() , email.get() , qualité.get()
    
    cur.execute("INSERT INTO ANNUAIRE(nom,prenom,tel,email,qualité) VALUES(?, ?, ?, ?, ?)" , datas)
    conn.commit()
    
    quitter()

def suprBDD():
    
    donneBD()        
    
    suppr = (BD[int(supr.get())-1][1],BD[int(supr.get())-1][2])
        
    cur.execute('DELETE FROM ANNUAIRE WHERE nom = ? AND prenom = ?', suppr)
    conn.commit()
    
    quitter()
    

def modifBDD() :
    donneBD()

    change = (modif.get(), BD[int(modifID.get())-1][1], BD[int(modifID.get())-1][2])
    
    cur.execute('UPDATE ANNUAIRE SET {} = ? WHERE nom = ? AND prenom = ?'.format(modifAT.get()), change)
    conn.commit()
    
    quitter()


conn = sqlite3.connect('Annuaire.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ANNUAIRE
                (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TECT, tel INT,
                email TEXT, qualité TEXT)""")

menu()
while choix != 5:
    if choix == 1:
       
        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit, bg = '#B0FCFD').pack(side = TOP, fill = X, pady = 5)

        Label(fenetre, text= 'Ajout à la base de donnée')
        
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
        
        donneBD()

        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit).pack(side = TOP, fill = X, pady = 5)
        
        Label(fenetre, text= 'Suprimer de la base de donnée').pack(side=TOP, pady=10)
        
        afficherBD()
        
        for i in range(len(BD)):
            ID.append(i+1)
        
        Label(fenetre, text= 'Que suprimer (ID) ?').pack(pady=5)

        supr = Combobox(fenetre, values=ID)
        supr.current(0)
        supr.pack(pady=5)
        
        Button(fenetre, text="Suprimer", command=suprBDD).pack(pady=5)
        
        Button(fenetre, text="Fermer", command=quitter).pack(pady=5)
               
        fenetre.mainloop()        

    elif choix == 3:
        
        ID = []
        
        donneBD()

        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit).pack(side = TOP, fill = X, pady = 5)
        
        Label(fenetre, text= 'Modifier la base de donnée').pack(side=TOP, pady=10)
        
        afficherBD()
        
        for i in range(len(BD)):
            ID.append(i+1)
        
        Label(fenetre, text= 'Que modifier (ID) ?').pack(pady=5)

        modifID = Combobox(fenetre, values=ID)
        modifID.current(0)
        modifID.pack()
        
        Label(fenetre, text= 'Quel atribut modifier ?').pack(pady=5)
        
        modifAT = Combobox(fenetre, values=['NOM', 'PRENOM', 'TELEPHONE', 'EMAIL', 'QUALITE'])
        modifAT.current(0)
        modifAT.pack()
        
        Label(fenetre, text= 'Par quelle valeur changer cet atribut ?').pack(pady=5)
        
        modif = Entry(fenetre)
        modif.pack(pady=5)
        
        Button(fenetre, text="Modifier", command=modifBDD).pack(pady=5)
        
        Button(fenetre, text="Fermer", command=quitter).pack(pady=5)
               
        fenetre.mainloop()        

    elif choix == 4:

        donneBD()

        fenetre = Tk()
        
        Button(fenetre, text="EXIT", command=Exit).pack(side = TOP, fill = X, pady = 5)
        
        Label(fenetre, text= 'Visualisation de la base de donnée').pack(side=TOP, pady=10)

        afficherBD()
        
        bouton=Button(fenetre, text="Fermer", command=quitter).pack(pady=5)

        fenetre.mainloop()
        
    if choix != 5:          
        menu() 
       

cur.close()
conn.close()
print("\nFin du programme")
#FIN