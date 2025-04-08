#Programme realise par BOUKLIKHA Mohamed-Amine => PC : 5
from tkinter import*
from random import *


#Creation de la fenetre
fenetre=Tk()
fenetre.title('TNSI_Bouklikha_Mohamed-Amine_jeu des potions')
fenetre.config(width=870, height=550)

fond = Canvas(fenetre,width=870, height=550, bg='skyblue')
fond.place(x=0,y=0)
canevas = Canvas(fond,width=515, height=400, bg='lightgreen')
canevas.place(x=60,y=80)

#Base avec les regles du jeu et les boutons
Titre = Label(fond, text="JEU DES POTIONS", font=('ARIAL',22,'bold'),fg='black',bg='lightgreen')
Titre.place(x=340,y=20)

regle = Canvas(fenetre,width=400, height=300, bg='brown')
regle_T = Label(regle, text="Regle du Jeu :", font=('times',20,'italic'),fg='white',bg='brown')
regle_T.place(x=30,y=10)
regle_text = Label(regle, text="Le but du jeu est de déplacer les disques d’une éprouvette                                                                                              \n"
                                "dans une autre de façon a avoir à la fin une seule couleurs                                                                                            \n"
                                "dans chaque éprouvette :                                                                                                                                                   \n"
                                ,font=('times',11,'italic'),fg='white',bg='brown')
regle_text.place(x=2,y=80)
regle_text2= Label(regle, text="• On ne peut déplacer d’une boule à la fois." ,font=('times',11,'italic'),fg='white',bg='brown')
regle_text2.place(x=10,y=150)
regle_text3= Label(regle, text="•  On ne peut prendre que la boule située au dessus." ,font=('times',11,'italic'),fg='white',bg='brown')
regle_text3.place(x=10,y=190)
regle_text4= Label(regle, text="• On peut mettre 3 boules max dans une même éprouvette." ,font=('times',11,'italic'),fg='white',bg='brown')
regle_text4.place(x=10,y=230)

#Class
class Maillon:
    def __init__(self, el, suivant):
        self.valeur = el
        self.suivant = suivant
class Pile:
    def __init__(self):
        self.element = None
    def Empile(self,e):
        self.element = Maillon(e, self.element)
    def Depile(self):
        if not self.EstVide():
            maillon = self.element
            self.element = maillon.suivant
            return maillon.valeur
        return None
    def EstVide(self):
        return self.element == None
    def __str__(self):
        text = "La pile est : "
        temp = self
        while not temp.EstVide():
            text = text+"\n"+"| "+str(temp.Depile())+" |"
        return text

#####################################################################################
#Fonctions:

def instructions():
    '''Permet d'afficher le canevas des regles du jeu'''
    regle.place(x=280,y=100)

def accueil():
    '''Permet de supprimer le canevas avec les regles et de revenir à l'accueil'''
    regle.place_forget()


# Fonction pour initialiser les éprouvettes avec des boules de debut choisis au hasard
def initialiser_eprouvettes():
    ''' Fonction pour initialiser les éprouvettes avec des boules de début choisies au hasard.'''
    global compteur_coups, eprouvette1, eprouvette2, eprouvette3, eprouvette4, eprouvette5
    eprouvette1 = Pile()
    eprouvette2 = Pile()
    eprouvette3 = Pile()
    eprouvette4 = Pile()
    eprouvette5 = Pile()
    canevas.delete('all')
    eprouvettes()
    compteur_coups = 0
    couleurs_boules = [ 'red', 'red', 'red', 'yellow', 'yellow', 'yellow','blue', 'blue', 'blue', 'green', 'green',
                       'green']  # liste des couleurs proposer lors du choix au hasard
    for e in range(3):
        placement = choice(couleurs_boules)
        couleurs_boules.remove(placement)
        eprouvette1.Empile(canevas.create_oval(x[0][0], y[e][0], x[0][1], y[e][1], fill=placement))
    for e in range(3):
        placement = choice(couleurs_boules)
        couleurs_boules.remove(placement)
        eprouvette2.Empile(canevas.create_oval(x[1][0], y[e][0], x[1][1], y[e][1], fill=placement))
    for e in range(3):
        placement = choice(couleurs_boules)
        couleurs_boules.remove(placement)
        eprouvette3.Empile(canevas.create_oval(x[2][0], y[e][0], x[2][1], y[e][1], fill=placement))
    for e in range(3):
        placement = choice(couleurs_boules)
        couleurs_boules.remove(placement)
        eprouvette4.Empile(canevas.create_oval(x[3][0], y[e][0], x[3][1], y[e][1], fill=placement))



def verifier():
    ''' Fonction pour vérifier si les éprouvettes ont une seule couleur dans chaque éprouvette.'''
    valeur_finale = True
    pile_temporaire = Pile()

    # Vérification de l'éprouvette 1
    couleurs = []
    couleur1, couleur2, couleur3 = None, None, None

    while not eprouvette1.EstVide():
        boule = eprouvette1.Depile()
        couleurs.append(canevas.itemcget(boule, 'fill'))
        pile_temporaire.Empile(boule)

    if len(couleurs) == 3:                                         #si c'est égale à trois couleur identiques
        couleur1 = couleurs[0]
        couleur2 = couleurs[1]
        couleur3 = couleurs[2]

    if not couleur3 == couleur2 == couleur1:                       #si ce n'est pas trois couleurs identiques
        valeur_finale = False

    while not pile_temporaire.EstVide():
        eprouvette1.Empile(pile_temporaire.Depile())

    # Vérification de l'éprouvette 2:
    couleurs = []
    couleur1, couleur2, couleur3 = None, None, None

    while not eprouvette2.EstVide():
        boule = eprouvette2.Depile()
        couleurs.append(canevas.itemcget(boule, 'fill'))
        pile_temporaire.Empile(boule)

    if len(couleurs) == 3:
        couleur1 = couleurs[0]
        couleur2 = couleurs[1]
        couleur3 = couleurs[2]

    if not couleur3 == couleur2 == couleur1:
        valeur_finale = False

    while not eprouvette2.EstVide():
        eprouvette2.Empile(pile_temporaire.Depile())

    # Vérification de l'éprouvette 3:
    couleurs = []
    couleur1, couleur2, couleur3 = None, None, None

    while not eprouvette3.EstVide():
        boule = eprouvette3.Depile()
        couleurs.append(canevas.itemcget(boule, 'fill'))
        pile_temporaire.Empile(boule)

    if len(couleurs) == 3:
        couleur1 = couleurs[0]
        couleur2 = couleurs[1]
        couleur3 = couleurs[2]

    if not couleur3 == couleur2 == couleur1:
        valeur_finale = False

    while not pile_temporaire.EstVide():
        eprouvette3.Empile(pile_temporaire.Depile())

    # Vérification de l'éprouvette 4:
    couleurs = []
    couleur1, couleur2, couleur3 = None, None, None

    while not eprouvette4.EstVide():
        boule = eprouvette4.Depile()
        couleurs.append(canevas.itemcget(boule, 'fill'))
        pile_temporaire.Empile(boule)

    if len(couleurs) == 3:
        couleur1 = couleurs[0]
        couleur2 = couleurs[1]
        couleur3 = couleurs[2]

    if not couleur3 == couleur2 == couleur1:
        valeur_finale = False

    while not pile_temporaire.EstVide():
        eprouvette4.Empile(pile_temporaire.Depile())

    # Vérification de l'éprouvette 5:
    couleurs = []
    couleur1, couleur2, couleur3 = None, None, None

    while not eprouvette5.EstVide():
        boule = eprouvette5.Depile()
        couleurs.append(canevas.itemcget(boule, 'fill'))
        pile_temporaire.Empile(boule)

    if len(couleurs) == 3:
        couleur1 = couleurs[0]
        couleur2 = couleurs[1]
        couleur3 = couleurs[2]

    if not couleur3 == couleur2 == couleur1:
        valeur_finale = False

    while not pile_temporaire.EstVide():
        eprouvette5.Empile(pile_temporaire.Depile())


    if valeur_finale == True:
        canevas.create_oval(10, 10, 510, 400,outline='blue', width=8)                    # Dessins du rond pour valider
    else:
        canevas.create_line(10, 10, 510, 400, fill='red', width=8)                       # Dessins de la croix
        canevas.create_line(10, 400, 510, 10, fill='red', width=8)



#POUR MONTER  :
def monter_boule_E1():
    '''Déplace une boule de l'eprouvette1 vers le stock '''
    if stock.EstVide():
        boule = eprouvette1.Depile()
        x_debut, y_debut = x[0][0], y[3][0]
        x_fin, y_fin = x[0][1], y[3][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        stock.Empile(boule)
        descendre()


def monter_boule_E2():
    '''Déplace une boule de l'eprouvette2 vers le stock '''
    if stock.EstVide():
        boule = eprouvette2.Depile()
        x_debut, y_debut = x[1][0], y[3][0]
        x_fin, y_fin = x[1][1], y[3][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        stock.Empile(boule)
        descendre()

def monter_boule_E3():
    '''Déplace une boule de l'eprouvette3 vers le stock '''
    if stock.EstVide():
        boule = eprouvette3.Depile()
        x_debut, y_debut = x[2][0], y[3][0]
        x_fin, y_fin = x[2][1], y[3][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        stock.Empile(boule)
        descendre()

def monter_boule_E4():
    '''Déplace une boule de l'eprouvette4 vers le stock '''
    if stock.EstVide():
        boule = eprouvette4.Depile()
        x_debut, y_debut = x[3][0], y[3][0]
        x_fin, y_fin = x[3][1], y[3][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        stock.Empile(boule)
        descendre()

def monter_boule_E5():
    '''Déplace une boule de l'eprouvette5 vers le stock '''
    if stock.EstVide():
        boule = eprouvette5.Depile()
        x_debut, y_debut = x[4][0], y[3][0]
        x_fin, y_fin = x[4][1], y[3][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        stock.Empile(boule)
        descendre()

def monter():
    '''Incrémente le compteur de coups, met à jour l'étiquette du compteur de coups et configure
     les commandes des boutons pour déplacer les boules vers le haut.'''
    global compteur_coups
    compteur_coups = compteur_coups + 1

    # Label pour le nombre de coup coup
    label_coup = Label(fond, text='Coups: '+ str(compteur_coups), font=('arial', 15, 'bold'), fg='black', bg='lightgreen')
    label_coup.place(x=680, y=70)

    B1.config(command=monter_boule_E1)
    B2.config(command=monter_boule_E2)
    B3.config(command=monter_boule_E3)
    B4.config(command=monter_boule_E4)
    B5.config(command=monter_boule_E5)


#POUR DESCENDRE :
def descendre_boule_E1():
    ''' Déplace une balle du stock vers l'eprouvette1 .'''
    pile_temporaire = Pile()
    compteur = 0

    while not eprouvette1.EstVide():
        pile_temporaire.Empile(eprouvette1.Depile())

    while not pile_temporaire.EstVide():
        eprouvette1.Empile(pile_temporaire.Depile())
        compteur = compteur + 1

    if not stock.EstVide():
        boule = stock.Depile()
        eprouvette1.Empile(boule)
        x_debut, y_debut = x[0][0], y[compteur][0]
        x_fin, y_fin = x[0][1], y[compteur][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        monter()



def descendre_boule_E2():
    ''' Déplace une balle du stock vers l'eprouvette2 .'''
    pile_temporaire = Pile()
    compteur = 0

    while not eprouvette2.EstVide():
        pile_temporaire.Empile(eprouvette2.Depile())
        compteur = compteur + 1

    while not pile_temporaire.EstVide():
        eprouvette2.Empile(pile_temporaire.Depile())

    if not stock.EstVide():
        boule = stock.Depile()
        eprouvette2.Empile(boule)
        x_debut, y_debut = x[1][0], y[compteur][0]
        x_fin, y_fin = x[1][1], y[compteur][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        monter()


def descendre_boule_E3():
    ''' Déplace une balle du stock vers l'eprouvette3 .'''
    pile_temporaire = Pile()
    compteur = 0

    while not eprouvette3.EstVide():
        pile_temporaire.Empile(eprouvette3.Depile())
        compteur = compteur + 1

    while not pile_temporaire.EstVide():
        eprouvette3.Empile(pile_temporaire.Depile())

    if not stock.EstVide():
        boule = stock.Depile()
        eprouvette3.Empile(boule)
        x_debut, y_debut = x[2][0], y[compteur][0]
        x_fin, y_fin = x[2][1], y[compteur][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        monter()

def descendre_boule_E4():
    ''' Déplace une balle du stock vers l'eprouvette4 .'''
    pile_temporaire = Pile()
    compteur = 0

    while not eprouvette4.EstVide():
        pile_temporaire.Empile(eprouvette4.Depile())
        compteur = compteur + 1

    while not pile_temporaire.EstVide():
        eprouvette4.Empile(pile_temporaire.Depile())

    if not stock.EstVide():
        boule = stock.Depile()
        eprouvette4.Empile(boule)
        x_debut, y_debut = x[3][0], y[compteur][0]
        x_fin, y_fin = x[3][1], y[compteur][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        monter()



def descendre_boule_E5():
    ''' Déplace une balle du stock vers l'eprouvette5 .'''
    pile_temporaire = Pile()
    compteur = 0

    while not eprouvette5.EstVide():
        pile_temporaire.Empile(eprouvette5.Depile())
        compteur = compteur + 1

    while not pile_temporaire.EstVide():
        eprouvette5.Empile(pile_temporaire.Depile())

    if not stock.EstVide():
        boule = stock.Depile()
        eprouvette5.Empile(boule)
        x_debut, y_debut = x[4][0], y[compteur][0]
        x_fin, y_fin = x[4][1], y[compteur][1]
        canevas.coords(boule, x_debut, y_debut, x_fin, y_fin)
        monter()

def descendre():
    ''' Configure les commandes des boutons pour déplacer les boules vers le bas.'''
    B1.config(command=descendre_boule_E1)
    B2.config(command=descendre_boule_E2)
    B3.config(command=descendre_boule_E3)
    B4.config(command=descendre_boule_E4)
    B5.config(command=descendre_boule_E5)


#Dessins des eprouvettes vides:
def eprouvettes():
    ''' Permet de positionner les éprouvettes sur le canevas '''
    # Eprouvette 1
    canevas.create_line(20, 150, 20, 355, fill="black", width=3)
    canevas.create_line(100, 151, 100, 355, fill="black", width=3)
    canevas.create_arc(100, 320, 20, 390, style=ARC, start=180, extent=180, fill="blue", outline="black", width=3)

    # Eprouvette 2
    canevas.create_line(120, 150, 120, 355, fill="black", width=3)
    canevas.create_line(200, 151, 200, 355, fill="black", width=3)
    canevas.create_arc(200, 320, 120, 390, style=ARC, start=180, extent=180, fill="blue", outline="black", width=3)

    # Eprouvette 3
    canevas.create_line(220, 150, 220, 355, fill="black", width=3)
    canevas.create_line(300, 151, 300, 355, fill="black", width=3)
    canevas.create_arc(300, 320, 220, 390, style=ARC, start=180, extent=180, fill="blue", outline="black", width=3)

    # Eprouvette 4
    canevas.create_line(320, 150, 320, 355, fill="black", width=3)
    canevas.create_line(400, 151, 400, 355, fill="black", width=3)
    canevas.create_arc(400, 320, 320, 390, style=ARC, start=180, extent=180, fill="blue", outline="black", width=3)

    # Eprouvette 5
    canevas.create_line(420, 150, 420, 355, fill="black", width=3)
    canevas.create_line(500, 151, 500, 355, fill="black", width=3)
    canevas.create_arc(500, 320, 420, 390, style=ARC, start=180, extent=180, fill="blue", outline="black", width=3)


#########################################################################################333

#Compteur pour le nombre de coups
compteur_coup = 0

# Création des piles représentant les éprouvettes
eprouvette1 = Pile()
eprouvette2 = Pile()
eprouvette3 = Pile()
eprouvette4 = Pile()
eprouvette5 = Pile()

#Coordonnees des placements des boules
x = [[25, 95], [125, 195], [225, 295], [325, 395], [425, 495]]
y = [[310, 380], [230, 300], [150, 220], [20, 90]]


#Pile qui stock les boule depile avant d'être réempiler
stock = Pile()


###################################################################################

#Boutons pour déplacer les boules
B1 = Button(fond, text="E1", font=('arial',10,'bold'),fg='black',bg='lightgrey',command=monter_boule_E1)
B1.place(x=105,y=505)
B2 = Button(fond, text="E2", font=('arial',10,'bold'),fg='black',bg='lightgrey',command=monter_boule_E2)
B2.place(x=205,y=505)
B3 = Button(fond, text="E3", font=('arial',10,'bold'),fg='black',bg='lightgrey',command=monter_boule_E3)
B3.place(x=305,y=505)
B4 = Button(fond, text="E4", font=('arial',10,'bold'),fg='black',bg='lightgrey',command=monter_boule_E4)
B4.place(x=405,y=505)
B5 = Button(fond, text="E5", font=('arial',10,'bold'),fg='black',bg='lightgrey',command=monter_boule_E5)
B5.place(x=505,y=505)


#Boutons
rejouer_btn = Button(fond, text="REJOUER", font=('arial',15,'bold'),fg='black',bg='lightgrey',command=initialiser_eprouvettes)
rejouer_btn.place(x=673, y=150)
valider_btn = Button(fond, text="VALIDER", font=('arial',15,'bold'),fg='black',bg='lightgrey',command=verifier)
valider_btn.place(x=680,y=250)
regle_btn = Button(fond, text="INSTRUCTIONS", font=('arial',15,'bold'),fg='black',bg='lightgrey',command=instructions)
regle_btn.place(x=650,y=350)
accueil_btn = Button(regle, text=" X ", font=('arial',10,'bold'),fg='white',bg='red',command=accueil)
accueil_btn.place(x=372,y=2)
accueil_btn.config(width=3,height=0,font=('ARIAL',8,'bold'))


# Appel de la fonction pour initialiser les éprouvettes au début
initialiser_eprouvettes()

fenetre.mainloop()