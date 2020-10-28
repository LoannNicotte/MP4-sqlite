import sqlite3
 
#---------------------------------------------------------------------------------------------------------------------------  

def menu():
    
    print(
"""
┌──────────────────────────────────────┐
│                                      │
│  1- Ajout à la base de donné         │
│  2- Supprimer de la base de donné    │
│  3- Modifier la base de donné        │
│  4- Recherche dans la base de donné  │
│  5- Voir la base de donné totale     │
│  6- Quitter le programme             │  
│                                      │
└──────────────────────────────────────┘  
""")

    
    choix = int(input("Quelle est votre choix ? \n"))
    while choix > 6 or choix < 1:
        print("Vous devez donnez soit 1;2;3;4 ou 4")
        choix = int(input("Quelle est votre choix ? \n"))
    return choix


def conectBDD():
    conn = sqlite3.connect('Annuaire.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS ANNUAIRE
                    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, prenom TECT, tel INT,
                    email TEXT, qualité TEXT)""")
  
def ajouterBDD(nom, prenom, tel,email,qualite):
    
    datas = nom , prenom , tel , email , qualite
    
    cur.execute("INSERT INTO ANNUAIRE(nom,prenom,tel,email,qualité) VALUES(?, ?, ?, ?, ?)" , datas)
    conn.commit()   

def suprBDD(colone, suppr):
    
    suppr=(suppr,)
        
    cur.execute('DELETE FROM ANNUAIRE WHERE {} = ?'.format(colone), suppr)
    conn.commit()

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
choix = menu()
while choix != 6:
    if choix == 1:
       
        nom = input("Nom \n")
        prenom = input("Prenom \n")
        tel = int(input("Telephone \n"))
        email = input("Email \n")
        qualité = input("Qualité \n")
        
        ajouterBDD(nom, prenom, tel,email,qualité)

    elif choix == 2:
        colone = input("Que voulez-vous supprimer ?\n"
                        "(nom, prenom, tel ,email, qualité)\n")
        suppr = input("Quelle est la donnée a supprimer ? \n")
        suprBDD(colone, suppr)        

    elif choix == 3:
        colone = input("Quelle colone modifier ?\n"
                        "(nom, prenom, tel ,email, qualité)\n")
        colone_connu = input("De quelle colone est la donnée connue ?\n"
                      "(nom, prenom, tel ,email, qualité)\n")
        ligne = input("Quelle est la donnée connu de {} ?\n".format(colone_connu))
        modif = input("Avec quelle donnée changer {} ? \n".format(colone))
        modifBDD(colone, colone_connu, ligne, modif)        

    elif choix == 4:
        colone = input("Quelle colone recherché ?\n"
                       "(nom, prenom, tel ,email, qualité, tous = *)\n")
        cond = input("Une condition ?")
        if cond == "non":
            ligne_cond = ""
            ligne_cond = ""
        else:
            colone_cond = input("Colone de la condition\n"
                                "(nom, prenom, tel ,email, qualité)\n")
            ligne_cond = input("A quoi est egale {} ?\n".format(colone_cond))        
        rechBDD(colone, colone_cond, ligne_cond, cond)
        
    elif choix == 5:
        cur.execute('SELECT * FROM ANNUAIRE')
        conn.commit()
        DB = cur.fetchall()
        print("")
        for i in range(len(DB)):
            print (DB[i])
        
        
    choix = menu()

cur.close()
conn.close()
print("\nFin du programme")