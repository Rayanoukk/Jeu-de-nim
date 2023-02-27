# Programme réalisé par: Chabchoub Salim, Oukaci, Rayan et Marchand Florian

import collections
from random import randint, random, seed
from fltk import *


#######################  fonctions des partie graphique  ####################
def appuie():
    '''
    simule l'evenement du click droit ou gauche
    :return : tuple
    '''
    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        # Action dépendant du type d'événement reçu :

        if tev == "ClicDroit":
            return(abscisse(ev), ordonnee(ev))

        elif tev == "ClicGauche":
            return(abscisse(ev), ordonnee(ev))

        elif tev == 'Quitte':  # on sort de la boucle
            break

        else:  # dans les autres cas, on ne fait rien
            pass

        mise_a_jour()


def ecran_acceuil(taille_fenetre):
    '''
    Affichage de la premiére page du jeu
    : param taille_fenetre : tuple
    : return : None
    '''
    x_0, y_0 = taille_fenetre
    ligne_1 = taille_fenetre[0] // 10  # constante pour les x
    ligne_2 = taille_fenetre[1] // 8   # constante pour les y 
    cree_fenetre(x_0, y_0)  
    police_titre = taille_fenetre[0] * 2 // 100
    police_txt = taille_fenetre[0] // 75
    texte((taille_fenetre[0] // 2 - police_titre), ligne_2, 'Jeu de nim', 'black', 'c', 'Helvetica', police_titre )  # pb taillepolice/pixel
    texte(ligne_1, 2 * ligne_2, 'Mode de Jeu : ', taille = taille_fenetre[0] // 65)

    texte(ligne_1, 3 * ligne_2, 'Normal : ', taille = police_txt)
    rectangle(2 * ligne_1, 3 * ligne_2, 2.5 * ligne_1 , 3.5 * ligne_2, 'black', 'black')

    texte(3 * ligne_1, 3 * ligne_2, 'De Marienbad : ', taille = police_txt)
    rectangle(4.5 * ligne_1, 3 * ligne_2, 5 * ligne_1, 3.5 * ligne_2)

    texte(6 * ligne_1, 3 * ligne_2, 'Rectangles : ', taille = police_txt)
    rectangle(6* ligne_1, 3.5 * ligne_2, 7 * ligne_1, 4 * ligne_2, 'black', 'black')

    texte(7.5 * ligne_1, 3 * ligne_2, '    Cercles  : ' , taille = police_txt )
    rectangle(7.5* ligne_1, 3.5 * ligne_2, 8.5 * ligne_1, 4 * ligne_2)

    texte(ligne_1, 4 * ligne_2, 'Normal : ', taille = police_txt)
    rectangle(2 * ligne_1, 4 * ligne_2, 2.5 * ligne_1, 4.5 * ligne_2, 'black', 'black')

    texte(3 * ligne_1, 4 * ligne_2, 'Misère : ', taille = police_txt)
    rectangle(4.5 * ligne_1, 4 * ligne_2, 5 * ligne_1, 4.5 * ligne_2)

    texte(ligne_1, 5 * ligne_2, '2 Joueurs : ', taille = police_txt)
    rectangle(2 * ligne_1, 5 * ligne_2, 2.5 * ligne_1, 5.5 * ligne_2, 'black', 'black')

    texte(3 * ligne_1, 5 * ligne_2, 'Ordinateur : ', taille = police_txt)
    rectangle(4.5 * ligne_1, 5 * ligne_2, 5 * ligne_1, 5.5 * ligne_2)

    texte(5 * ligne_1, 6 * ligne_2, 'Play', ancrage = 'c', taille = police_titre)
    image(ligne_1, ligne_2, 'settings.png', ancrage = 'center')


def menu(ligne_1, ligne_2, x, y):
    '''
    permet de modifier le mode de jeu dans la premiére page du jeu et de 
    choisir l'objet rectangle ou cercle
    : param ligne_1 , ligne_2 , x , y : int
    : return mode_jeu : list
    ''' 

    if x > 2 * ligne_1 and y > 3 * ligne_2 and x < 2.5 * ligne_1 and y < 3.5 * ligne_2:  # dans rectangle 'normal'
        mode_jeu[0] = 'normal'
        rectangle(2 * ligne_1, 3 * ligne_2, 2.5 * ligne_1 , 3.5 * ligne_2, 'black', 'black')  # case 'normal' devient noir
        rectangle(4.5 * ligne_1, 3 * ligne_2, 5 * ligne_1, 3.5 * ligne_2, 'black', 'white')  # case 'de marienbad' redevient transparente si elle etait noire

    elif x > 4.5 * ligne_1 and y > 3 * ligne_2 and x < 5 * ligne_1 and y < 3.5 * ligne_2:  # dans case 'de marienbad'
        mode_jeu[0] = 'marienbad'
        rectangle(4.5 * ligne_1, 3 * ligne_2, 5 * ligne_1, 3.5 * ligne_2, 'black', 'black')  # case 'de maienbad' devient noir
        rectangle(2 * ligne_1, 3 * ligne_2, 2.5 * ligne_1 , 3.5 * ligne_2, 'black', 'white')  # case 'normal' redevient transparente si elle etait noire
    if x > 6 * ligne_1 and y > 3.5 * ligne_2 and x < 7 * ligne_1 and y < 4 * ligne_2 :
        mode_jeu[3] = 'rectangle'
        rectangle(6* ligne_1, 3.5 * ligne_2, 7* ligne_1, 4 * ligne_2 ,'black','black')
        rectangle(7.5* ligne_1, 3.5 * ligne_2, 8.5 * ligne_1, 4 * ligne_2, 'black', 'white')
    if x > 7.5 * ligne_1 and y > 3.5 * ligne_2 and x < 8.5 * ligne_1 and y < 4 * ligne_2 :
        mode_jeu[3] = 'cercle'
        rectangle(6* ligne_1 , 3.5 * ligne_2 , 7* ligne_1 , 4 * ligne_2 , 'black', 'white')
        rectangle(7.5* ligne_1, 3.5 * ligne_2, 8.5 * ligne_1, 4 * ligne_2, 'black', 'black')
    
    if x > 2 * ligne_1 and y > 4 * ligne_2 and x < 2.5 * ligne_1 and y < 4.5 * ligne_2:
        mode_jeu[1] = 'normale'
        rectangle(2 * ligne_1, 4 * ligne_2, 2.5 * ligne_1, 4.5 * ligne_2, 'black', 'black')
        rectangle(4.5 * ligne_1, 4 * ligne_2, 5 * ligne_1, 4.5 * ligne_2, 'black', 'white')

    if x > 4.5 * ligne_1 and y > 4 * ligne_2 and x < 5 * ligne_1 and y < 4.5 * ligne_2:
        mode_jeu[1] = 'misere'
        rectangle(4.5 * ligne_1, 4 * ligne_2, 5 * ligne_1, 4.5 * ligne_2, 'black', 'black')
        rectangle(2 * ligne_1, 4 * ligne_2, 2.5 * ligne_1, 4.5 * ligne_2, 'black', 'white')
    
    if x > 2 * ligne_1 and y > 5 * ligne_2 and x < 2.5 * ligne_1 and y < 5.5 * ligne_2:
        mode_jeu[2] = '2 joueur'
        rectangle(2 * ligne_1, 5 * ligne_2, 2.5 * ligne_1, 5.5 * ligne_2, 'black', 'black')
        rectangle(4.5 * ligne_1, 5 * ligne_2, 5 * ligne_1, 5.5 * ligne_2, 'black', 'white')
    if x > 4.5 * ligne_1 and y > 5 * ligne_2 and x < 5 * ligne_1 and y < 5.5 * ligne_2:
        mode_jeu[2] = 'ordi'
        rectangle(4.5 * ligne_1, 5 * ligne_2, 5 * ligne_1, 5.5 * ligne_2, 'black', 'black')
        rectangle(2 * ligne_1, 5 * ligne_2, 2.5 * ligne_1, 5.5 * ligne_2, 'black', 'white')
    
    #ferme_fenetre()
    
    return  mode_jeu


def menu_para(taille_fenetre, mode_jeu):
    '''
    Choix des parametres de jeu
    param: mode de jeu (tuples) 
    return: nb_obj (int), diff_bot (booleen) ou lst (liste), diff_bot (booleen)
    '''
    x_0, y_0 = taille_fenetre
    cree_fenetre(x_0, y_0)
    ligne_1 = taille_fenetre[0] // 10  # constante pour les x
    ligne_2 = taille_fenetre[1] // 8 
    police_titre = taille_fenetre[0] * 2 // 100
    police_txt = taille_fenetre[0]  // 75

    texte(ligne_1, ligne_2, 'Menu des paramètres : ', taille = police_titre)
    
#############################  Parametre normal  ####################

    if mode_jeu[0] == 'normal':
        txt_0 = texte(ligne_1, 2 * ligne_2, 'combien de batons ?', taille = police_txt)  # entrer nb obj
        rect_0 = rectangle(3 * ligne_1, 2 * ligne_2, 4 * ligne_1 , 2.5 * ligne_2)
        texte(5 * ligne_1, 6 * ligne_2, 'Play', ancrage = 'c', taille = police_titre)  # Play

        var, nb_obj = saisie_controler(3 * ligne_1, 2 * ligne_2)  # saisie controlée du nombre d'objet
        while not var:
            var, nb_obj = saisie_controler(3 * ligne_1, 2 * ligne_2)

        efface(txt_0)
        efface(rect_0)
        txt_0 =  texte(ligne_1, 2 * ligne_2, 'Coup max :', taille = police_txt)
        rect_0 = rectangle(3 * ligne_1, 2 * ligne_2, 4 * ligne_1 , 2.5 * ligne_2)
        var, coup_max = saisie_controler(3 * ligne_1, 2 * ligne_2)  # saisie controlée du nombre d'objet
        while not var:
            var, coup_max = saisie_controler(3 * ligne_1, 2 * ligne_2)
        efface(txt_0)
        efface(rect_0)
        texte(ligne_1 , 2 * ligne_2 , 'Paramètre mode normal validé', taille = police_txt)
        

        diff_bot = None
        if mode_jeu[2] == 'ordi':
            diff_bot = 'facile'
            texte(ligne_1 , 3 * ligne_2 , "Difficulté du bot :", taille = police_txt)
            rectangle(3 * ligne_1, 3 * ligne_2, 4 * ligne_1, 3.5 * ligne_2, 'black', 'black')
            texte(3 * ligne_1, 3 * ligne_2, '    Facile',"white", taille = police_txt)
            rectangle(4.5 * ligne_1, 3 * ligne_2, 5.5 * ligne_1, 3.5 * ligne_2)
            texte(4.5 * ligne_1, 3 * ligne_2, '      Dur', "black", taille = police_txt)
    
            x, y = appuie()
            while x < 4.5 * ligne_1 or x > 5.5 * ligne_1 or y < 5.75 * ligne_2 or y > 6.25 * ligne_2:  # hors du rectangle 'Play'
                x, y = appuie()
                if x > 3 * ligne_1 and y > 3 * ligne_2 and x < 4 * ligne_1 and y < 3.5 * ligne_2:  # clic dans diffi du bot
                    diff_bot = 'facile'
                    rectangle(3 * ligne_1, 3 * ligne_2, 4 * ligne_1 , 3.5 * ligne_2, 'black', 'black')
                    rectangle(4.5 * ligne_1, 3 * ligne_2, 5.5 * ligne_1, 3.5 * ligne_2, 'black', 'white')  # besoin transparent
                    texte(3 * ligne_1, 3 * ligne_2, '    Facile',"white", taille = police_txt)
                    texte(4.5 * ligne_1, 3 * ligne_2, '      Dur',"black", taille = police_txt)

                elif x > 4.5 * ligne_1 and y > 3 * ligne_2 and x < 5.5 * ligne_1 and y < 3.5 * ligne_2:
                    diff_bot = 'dur'
                    rectangle(3 * ligne_1, 3 * ligne_2, 4 * ligne_1 , 3.5 * ligne_2, 'black', 'white')  # besoin transparent
                    rectangle(4.5 * ligne_1, 3 * ligne_2, 5.5 * ligne_1, 3.5 * ligne_2, 'black', 'black')
                    texte(3 * ligne_1, 3 * ligne_2, '    Facile', "black", taille = police_txt)
                    texte(4.5 * ligne_1, 3 * ligne_2, '      Dur', "white", taille = police_txt)

        x, y = appuie()
        while x < 4.5 * ligne_1 or x > 5.5 * ligne_1 or y < 5.75 * ligne_2 or y > 6.25 * ligne_2:  # hors du rectangle 'Play'
            x, y = appuie()

        #ferme_fenetre()
        return nb_obj, diff_bot, coup_max
    
############################  Parametre marienbad ##################

    if mode_jeu[0] == 'marienbad' :  
        texte(4.5 * ligne_1, 6 * ligne_2, 'Play', taille = police_titre)
        txt_0 = texte(ligne_1, 2 * ligne_2, 'combien de rangées ?', taille = police_txt)
        rect_0 = rectangle(3 * ligne_1, 2 * ligne_2, 4 * ligne_1, 2.5 * ligne_2)
        var, val = saisie_controler(3 * ligne_1, 2 * ligne_2)
        while not var:
            var, val = saisie_controler(3 * ligne_1, 2 * ligne_2)
        efface(txt_0)
        efface(rect_0)
        
        lst = [0] * val
        for i in range(val):
            txt = texte(ligne_1, 2 * ligne_2, f"combien d'objet dans la rangée {i+1} ?", taille = police_txt)
            rect = rectangle(4.5 * ligne_1, 2 * ligne_2, 5.5 * ligne_1, 2.5 * ligne_2)
            var, nb_obj = saisie_controler(4.5 * ligne_1, 2 * ligne_2)
            while not var:
                var, nb_obj = saisie_controler(4.5 * ligne_1, 2 * ligne_2)

            lst[i] = nb_obj # rentrer les valeurs dans la liste
            efface(txt)  # effacer la ligne avant afficher la suivante
            efface(rect)
        texte(ligne_1, 2 * ligne_2, "fin des paramètres marienbad", taille = police_txt)

        
        diff_bot = None
        if mode_jeu[2] == 'ordi':
            diff_bot = 'facile'
            texte(ligne_1, 4 * ligne_2, "Difficulté du bot :", taille = police_txt)
            rectangle(3 * ligne_1, 4 * ligne_2, 4 * ligne_1 , 4.5 * ligne_2, 'black', 'black')
            texte(3 * ligne_1, 4 * ligne_2, '    Facile', 'white', taille = police_txt)
            rectangle(4.5 * ligne_1, 4 * ligne_2, 5.5 * ligne_1, 4.5 * ligne_2)
            texte(4.5 * ligne_1, 4 * ligne_2, '      Dur', taille = police_txt)

            x, y = appuie()
            while x < 4.5 * ligne_1 or x > 5 * ligne_1 or y < 6 * ligne_2 or y > 6.5 * ligne_2:  # hors du rectangle 'Play'
                x, y = appuie()

                if x > 3 * ligne_1 and y > 4 * ligne_2 and x < 4 * ligne_1 and y < 4.5 * ligne_2:
                    diff_bot = 'facile'
                    rectangle(3 * ligne_1, 4 * ligne_2, 4 * ligne_1 , 4.5 * ligne_2, 'black', 'black')
                    rectangle(4.5 * ligne_1, 4 * ligne_2, 5.5 * ligne_1, 4.5 * ligne_2, 'black', 'white')
                    texte(3 * ligne_1, 4 * ligne_2, '    Facile', "white", taille = police_txt)
                    texte(4.5 * ligne_1, 4 * ligne_2, '      Dur', "black", taille = police_txt)

                elif x > 4.5 * ligne_1 and y > 4 * ligne_2 and x < 5.5 * ligne_1 and y < 4.5 * ligne_2:
                    diff_bot = 'dur'
                    rectangle(3 * ligne_1, 4 * ligne_2, 4 * ligne_1, 4.5 * ligne_2, 'black', 'white')
                    rectangle(4.5 * ligne_1, 4 * ligne_2, 5.5 * ligne_1, 4.5 * ligne_2, 'black', 'black')
                    texte(3 * ligne_1, 4 * ligne_2, '    Facile', "black", taille = police_txt)
                    texte(4.5 * ligne_1, 4 * ligne_2, '      Dur', "white", taille = police_txt)

        else:
            x, y = appuie()

        while x < 4.5 * ligne_1 or x > 5 * ligne_1 or y < 6 * ligne_2 or y > 6.5 * ligne_2:  # hors du rectangle 'Play' (touché controlé)
            x, y = appuie()
        
        #ferme_fenetre()
        return lst ,diff_bot


def dessin_du_jeu(taille_fenetre, l, nb_objet, mode_jeu):
    '''
    dessine les objets du jeu et exécute graphiquement le jeu du joueur ou du
    bot
    : param taille_fenetre , l, nb_objet , mode_jeu : tuple , list ,int , list
    : return : l 
    '''
    typmode = mode_jeu[0]
    x_0, y_0 = taille_fenetre
    ligne_1 = taille_fenetre[0] // 20  # constante pour les x
    ligne_2 = taille_fenetre[1] // 20  # constante pour les y  
    cree_fenetre(x_0, y_0)
    rectangle(0, 0, x_0, y_0, couleur='black', remplissage = 'black')
    if(typmode == 'marienbad'):
        lst = []
        for i in range(len(l)):
            lst.append([None]* l[i]) # pour permettre d'enregistrer les rectangles 4

        if(mode_jeu[3] == 'rectangle'):
            e = 0 
            i = 1
            nb = 0
            mm = 0
            while (i != len(l) +  1):
                for j in range(1, l[e] + 1):
                    lst[e][j - 1] =  rectangle((ligne_1 * mm), (ligne_2 * i) + nb, (ligne_1 * mm) + 15, (ligne_2 * i) + nb + 15, couleur = 'black', remplissage= 'white')
                    mm += 0.5
                mm = 0
                i += 1
                e += 1
                nb += 5
        elif(mode_jeu[3] == 'cercle'):
            e = 0 
            i = 1
            nb = 0
            mm = 0.5
            while (i != len(l) + 1):
                for j in range(1, l[e] + 1 ):
                    lst[e][j - 1] =  cercle((ligne_1 * mm), (ligne_2 *(i + 1) ) + nb, 8.25, couleur='black', remplissage='yellow')
                    mm += 0.51
                mm = 0.5
                i += 1
                e += 1
                nb += 5  

        return lst # return une liste qui contient tout les rectangles
    else :
        lst = []
        if(mode_jeu[3] == 'rectangle'):
            e = 0
            for i in range(nb_objet):
                lst.append(rectangle(ligne_1 * e, (y_0 // 2), ligne_1 * e + 17, (y_0 // 2 ) + 17 , 'black' , 'white'))
                e += 0.5
        elif(mode_jeu[3] == 'cercle'):
            e = 0.3
            for i in range(nb_objet) :
                lst.append(cercle(ligne_1 * e, (y_0 // 2), 10, couleur='black', remplissage='yellow'))
                e += 0.5
        return lst

def jeudujoeuree(taille_fenetre, mode_jeu):
    '''
    permet de poser des questions à l'utilisateur et reçoit ce qu'il saisit
    : param taille_fenetre , mode_jeu : tuple , list
    : return nb_objet , rangee : int
    '''
    x0 = taille_fenetre[0]
    x1 = taille_fenetre[1]
    ligne_1 = x0 // 20
    ligne_2 = x1 // 20
    police_titre = x0 * 2 // 200
    police_txt = x0  // 75
    if(mode_jeu[0] == 'marienbad') :
        txt_0 = texte(ligne_1 * 8, ligne_2 * 0, f'joueur {nb + 1} quelle rangée vous voulez choisir ?', couleur='white', taille= police_txt, ancrage= 'n')  # entrer nb obj
        rect_0 = rectangle(12 * ligne_1, 0 * ligne_2, 13 * ligne_1, 1 * ligne_2, couleur='white', remplissage='white')

        var, rangee = saisie_controler(12* ligne_1, 0 * ligne_2)  # saisie controlée du nombre d'objet
        while not var:
            var, rangee = saisie_controler(12 * ligne_1, 0 * ligne_2)

        efface(txt_0)
        efface(rect_0)
        txt_0 = texte(ligne_1 * 8, ligne_2 * 0, "combien d'objet vous voulez prendre de cette rangée?", couleur='white', taille= police_txt, ancrage= 'n')  # entrer nb obj
        rect_0 = rectangle(13 * ligne_1, 0 * ligne_2, 14 * ligne_1, 1 * ligne_2, couleur='white', remplissage='white')
        var, nb_obj = saisie_controler(13 * ligne_1, 0 * ligne_2)  # saisie controlée du nombre d'objet
        while not var:
            var, nb_obj = saisie_controler(13 * ligne_1, 0 * ligne_2)

        efface(txt_0)
        efface(rect_0)


        return nb_obj, rangee
    else:
        txt_0 = texte(ligne_1 * 8, ligne_2 * 0, f"joueur {nb + 1} combien d'objet voulez vous prendre ?", couleur= 'white', taille= police_txt, ancrage = 'n')  # entrer nb obj
        rect_0 = rectangle(13 * ligne_1, 0 * ligne_2, 14 * ligne_1 , 1 * ligne_2 , couleur='white' , remplissage='white')
        var, nb_obj = saisie_controler(13 * ligne_1, 0 * ligne_2)  # saisie controlée du nombre d'objet
        while not var :
            var, nb_obj = saisie_controler(13 * ligne_1, 0 * ligne_2)

        efface(txt_0)
        efface(rect_0)
        return nb_obj


def input_graphique(x, y):  # a remplacer au niveau des inputs
    '''
    permet d'entrer des touches du clavier via la partie graphique
    param: x, y deux coordonnées
    return: str
    '''
    police_txt = taille_fenetre[0]  // 75
    nb = ''
    txt = ''
    while True:
        ev = donne_ev()
        if type_ev(ev) == 'Touche':
            if touche(ev) == 'Return':
                efface(txt)
                return nb
            elif touche(ev) == 'BackSpace':
                nb_2 = ''
                if len(nb) > 0:
                    efface(txt)
                    for i in range(len(nb) - 1):
                        nb_2 += nb[i]
                    nb = nb_2
                    txt = texte(x, y, f'{nb}', taille = police_txt)
                
            
            else:
                efface(txt)
                nb += touche(ev)
                txt = texte(x, y, f'{nb}', taille = police_txt)
            
        mise_a_jour()


def saisie_controler(x, y):
    '''
    Prend en compte une saisie du clavier et dit s'il s'agit d'un nombre
    param: x, y deux coordonnées
    return: booleen et int
    '''
    var = input_graphique(x, y)
    while len(var) == 0:
        var = input_graphique(x, y)
    for elem in var:
        if elem not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False, var
    var = int(var)
    return True, var

#  ------------- Normal-----------------------
def coup_possible_normal(nb_objet, coup_max):
    '''
    Renvoie la liste des coup possible
    return : liste 
    >>> nb_objet = 21
    >>> coup_max = 3
    >>> coup_possible_normal(nb_objet,coup_max)
    [1, 2, 3]
    >>> nb_objet = 2
    >>> coup_max = 3 
    >>> coup_possible_normal(nb_objet,coup_max)
    [1, 2]
    '''
    lst = []
    if nb_objet >= coup_max:
        lst.extend(list(range(1, coup_max + 1)))
    if nb_objet < coup_max:
        lst.extend(list(range(1, nb_objet + 1)))
    return lst


def strategie_normale_normale(nb_objet, coup_max):
    '''
    simule le jeu du bot quand le mode est dure dans le mode normale normale
    : param nb_objet , coup_max : int
    : return : int
    >>> nb_objet = 21
    >>> coup_max = 4
    >>> strategie_normale_normale(nb_objet, coup_max)
    1
    >>> nb_objet = 38
    >>> coup_max = 4
    >>> strategie_normale_normale(nb_objet, coup_max)
    3
    >>> seed(41)
    >>> nb_objet = 28
    >>> coup_max = 3
    >>> strategie_normale_normale(nb_objet, coup_max)
    2
    '''
    if nb_objet % (coup_max + 1) != 0:
        return nb_objet % (coup_max + 1)
    else:
        return randint(1, coup_max)


def strategie_normal_misére(nb_objet, coup_max):
    '''
    simule le jeu du bot quand le mode est dure dans le mode normale misére
    : param nb_objet , coup_max : int
    : return : int
    >>> nb_objet = 18
    >>> coup_max = 3
    >>> strategie_normal_misére(nb_objet, coup_max)
    1
    >>> nb_objet = 39
    >>> coup_max = 4
    >>> strategie_normal_misére(nb_objet, coup_max)
    3
    >>> seed(15468)
    >>> nb_objet = 25
    >>> coup_max = 5
    >>> strategie_normal_misére(nb_objet, coup_max)
    4
    '''
    if nb_objet % (coup_max + 1) != 1 and nb_objet % (coup_max + 1) != 0:
        return (nb_objet % (coup_max + 1)) - 1
    if nb_objet % (coup_max + 1) == 0:
        return coup_max
    if nb_objet % (coup_max + 1) == 1 :
        temp = randint(1, coup_max)
        while temp not in coup_possible_normal(nb_objet, coup_max):
            temp = randint(1, coup_max)
        return temp


def coup_jouer_normal(nb_objet, coup, coup_max):
    '''
    joue le coup et modifie le nombre d'objet sur la table
    param : nombres entiers (int)
    return : nombre entier (int) 
    >>> coup_jouer(21, 3, 3)
    18
    >>> coup_jouer(21, 5, 3)
    None
    '''
    if coup in coup_possible_normal(nb_objet, coup_max):
        nb_objet -= coup
        return nb_objet
    return None  # si le coup n'est pas possible renvoie None ( ==> boucle While )

    
def victoire_normal(nb_objet):
    '''
    return True si un joueur a gagner
    param : nombre entier (int)
    return : booléen
    >>> nb_objet = 1
    >>> victoire(nb_objet)
    False
    >>> nb_objet = 0
    >>> victoire(nb_objet)
    True
    '''
    if nb_objet == 0:
        return True
    else:
        return False

#  -------------- Marienbad---------------------
def coup_possible_marienbad(l):
    '''
    Renvoie la liste des coup possible
    return : liste de listes
    >>> l = [7, 5, 3, 1]
    >>> coup_possible()
    [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5], [1, 2, 3], [1]]

    '''
    lst = []
    for i in range(len(l)):
        lst.append(list(range(1, l[i] + 1)))
    return lst


def coup_jouer_marienbad(l, coup, rangee):
    '''
    joue le coup et modifie le nombre d'objet sur la table
    param : nombres entiers (int)
    return : nombre entier (int) 
    >>> coup_jouer([7,5,3,1], 3, 1)
    [4, 5, 3, 1]
    >>> coup_jouer([7, 5, 3, 1], 5, 3)
    None
    '''
    if(rangee > len(l)):
        return None
    elif coup in (coup_possible_marienbad(l))[rangee - 1]:
        l[rangee - 1] -= coup
        return l
    # si le coup n'est pas possible renvoie None ( ==> boucle While )
    return None


def victoire_marienbad(l):
    '''
    return True si un joueur a gagner
    param : nombre entier (int)
    return : booléen
    >>> l = [0, 5, 3, 1]
    >>> victoire(nb_objet)
    False
    >>> l = [0, 0, 0, 0]
    >>> victoire(nb_objet)
    True
    '''
    for i in range(len(l)):
        if(l[i] != 0):
            return False
    return True


def deci_bin_marienbad(l):
    ''' Transforme la liste des nombres decimaux en binaires 

    >>> deci_bin([1,2,3,4])
    [1, 10, 11, 100]
    >>> deci_bin([0, 0, 0, 0])
    >>> [0, 0, 0, 0]
    '''
    lst = []
    for i in range(len(l)):
        q = l[i]
        s = ''
        r = 0
        if(q == 0):
            lst.append(0)
        else:
            while(q != 0):
                r = q % 2
                q = q // 2
                s = f'{r}' + s
            lst.append(int(s))
    return lst


def si_pair_marienbad(somme):
    ''' verifie si somme contient que des nombres paires
    >>> si_pair (74)
    False
    >>> si_pair(84)
    True

    '''
    if(type(somme) == int):
        somme = str(somme)
    for i in range(len(somme)):
        if (int(somme[i]) % 2 != 0) or (int(somme[i]) == 1):
            return False
    return True


def gagnante_ou_pas_marienbad(l):
    '''
    verifie si la combinaison passé est gangnante ou pas
    
    '''
    lst = deci_bin_marienbad(l)
    somme = 0
    for i in range(len(lst)):
        somme += lst[i]
    return si_pair_marienbad(somme)


def strategie_marienbad_normale(l):
    '''
    simule le jeu du bot pour le mode de marienbad normale pour une difficulté dur
    :param l : list
    :return : tuple
    '''
    if gagnante_ou_pas_marienbad(l):
        i = randint(0, len(l) - 1)
        while(l[i] == 0):
            i = randint(0, len(l) - 1)  # pour eviter le  randint (1 ,0)
        coup = randint(1, l[i])
        l[i] -= coup
        return coup, i
    else:
        j = list(l)
        i = 0
        nb = 1  # compte le nombre a retiré
        premiervaleur = j[i]
        while(gagnante_ou_pas_marienbad(j) != True):
            if(j[i] != 0):
                j[i] = l[i] - nb
                nb += 1
            elif i != len(l):
                j[i] = premiervaleur
                i += 1
                nb = 1
                premiervaleur = j[i]
        l[i] -= nb-1
        return nb - 1, i


def savoirsilafin_marienbad(l):
    '''  
    verifie si on est arriver presque à la fin de la partie c'est à dire une
    une situation pour changer la stratégie pour gagner le mode misére
    : param l : list
    : return :boolean , int
    
    '''
    nb = 0
    for i in range(len(l)):
        if(l[i] != 0) and (l[i] != 1):
            nb += 1
    if(nb != 1):
        return False , 0
    return True, nb


def sommedesnon0_marienbad(l):

    '''
    compte la somme  des chiffres different de 0 dans la liste
    : param l:list
    : return : int 
    '''
    nb = 0
    for i in range(len(l)):
        if(l[i] == 1):
            nb += 1
    return nb + (savoirsilafin_marienbad(l))[1]


def savoir1ou0_marienbad(l):
    '''
    verifie si la liste ne contient que des 1 et des 0
    : param l:list
    : return : boolean
    '''
    for i in range(len(l)):
        if(l[i] != 0 ) or (l[i] != 1):
            return False
    return True


def strategie_marienbad_misere(l):
    '''
    simule le jeu du bot pour le mode de marienbad misere pour une difficulté dur
    :param l : list
    :return : tuple
    '''
    if(savoirsilafin_marienbad(l))[0]:
        if(sommedesnon0_marienbad(l) % 2 == 0):
            for i in range(len(l)):
                if l[i] != 0 and l[i] != 1:
                    a = l[i]
                    l[i] -= a
                    return a, i
        else:
            for i in range(len(l)):
                if l[i] != 0 and l[i] != 1:
                    a = l[i] - 1
                    l[i] -= a
                    return a, i
    else:
        if(savoir1ou0_marienbad(l)):
                for i in range(len(l)):
                    if(l[i] == 1):
                        a = l[i]
                        l[i] -= a
                        return a, i
        else:
            return strategie_marienbad_normale(l)


def bot_facile(mode_jeu , coup_max , l):
    '''
    simule le jeu du bot quand la difficulté est facile
    :param mode_jeu , coup_max ,l : list , int,list
    :return value : int
    >>> seed(41)
    >>> l=[5,4,6,7]
    >>> mode_jeu = ['normal','normale','ordi']
    >>> coup_max = 3
    >>> bot_facile(mode_jeu, coup_max,l)
    2
    >>> seed(41)
    >>> l=[5,4,6,7]
    >>> coup_max = 3
    >>> mode_jeu = ['marienbad','normale','ordi']
    >>> bot_facile(mode_jeu, coup_max,l)
    (3, 3)
    '''
    if mode_jeu[0] == 'normal':
        temp = randint(1, coup_max)
        while temp not in coup_possible_normal(nb_objet,coup_max):
            temp = randint(1, coup_max)
        return temp
    else:
        r = randint(0, len(l) - 1)
        while(l[r] == 0):
            r = randint(0, len(l) - 1)  # pour eviter le  randint (1 ,0)
        coup = randint(1, l[r])
        while coup not in coup_possible_marienbad(l)[r]:
            coup = randint(1, l[r])
        l[r] -= coup
        return coup, r


if __name__ == "__main__" :
    while True :
        ########################## Variable par défaut #######################
        taille_fenetre = 800, 600
        mode_jeu = ['normal', 'normale', '2 joueurs', 'rectangle']
        police_txt = taille_fenetre[0]  // 75
        l=[7, 5, 3, 1]
        nb_objet = 21
        coup_max = 3
        diff_bot = 'facile'
        ######################################################################
        ecran_acceuil(taille_fenetre)
        ligne_1 = taille_fenetre[0] // 10  # constante pour les x
        ligne_2 = taille_fenetre[1] // 8   # constante pour les y 
        x, y = appuie()
        while x < 4.5 * ligne_1 or x > 5.5 * ligne_1 or y < 5.75 * ligne_2 or y > 6.5 * ligne_2:  # hors du rectangle 'Play'
            x, y = appuie()
            if x > 0.5 * ligne_1 and y > 0.5 * ligne_2 and x < 1.25 * ligne_1 and y < 1.5 * ligne_2 :  # clique sur le bouton paramètre
                ferme_fenetre()
                if mode_jeu[0] == 'normal':
                    nb_objet, diff_bot, coup_max = menu_para(taille_fenetre, mode_jeu)
                    l = [1]       
                else:
                    l, diff_bot = menu_para(taille_fenetre, mode_jeu)
                break
            else :  #  la zone de mode de jeu
                mode_jeu = menu(ligne_1 , ligne_2 , x , y)       
        ferme_fenetre()
        print(mode_jeu)
        print(l)
        nb = randint(0, 1)  # generateur aleatoire du premier joueur
        lst = dessin_du_jeu((taille_fenetre[0], taille_fenetre[1]), l, nb_objet, mode_jeu  )
        x , y = appuie()
        while not victoire_marienbad (l)  and not victoire_normal(nb_objet) :
                # partie graphique
            mise_a_jour()
            nb = 1 - nb    # ordinateur(bot)
            if nb == 1 and mode_jeu[1] == 'normale' and mode_jeu[2] == 'ordi':
                if mode_jeu[0] == 'marienbad' :
                    attente(1)
                    if diff_bot == 'dur':
                        coup, rangee = strategie_marienbad_normale(l)
                    else:
                        coup, rangee = bot_facile(mode_jeu , coup_max , l)
                    txt_4 = texte(ligne_1 * 5, ligne_2 * 0, f'le bot a pris {coup} de la rangée {rangee + 1}', couleur="white", taille= police_txt, ancrage= 'n')
                    print(coup, rangee)
                    print(f'le bot a joué {coup} dans la rangée {rangee + 1} ')
                    print(l)
                    for i in range(coup):
                        efface(lst[rangee][len(lst[rangee]) - 1 ] )
                        lst[rangee].pop()
                    attente(2)
                    efface(txt_4)
                elif mode_jeu[0] == 'normal' :
                    attente(1)
                    if diff_bot == 'dur':
                        coup = strategie_normale_normale(nb_objet, coup_max)
                    else:
                        coup = bot_facile(mode_jeu, coup_max, l)
                    txt_2 = texte(ligne_1 * 5, ligne_2 * 2, f'le bot a pris {coup} objet(s)', couleur='white', taille= police_txt, ancrage= 'n')
                    print(f'le bot a joué {coup}')
                    nb_objet -= coup
                    print( f'il reste {nb_objet} objet ')
                    for i in range(coup):
                        efface(lst[len(lst) - 1 ])
                        lst.pop()
                    attente(2)
                    efface(txt_2)
            elif nb == 1 and mode_jeu[1] == 'misere' and mode_jeu[2] == 'ordi':
                if mode_jeu[0] == 'marienbad' :
                    attente(1)
                    if diff_bot == 'dur':
                        coup, rangee = strategie_marienbad_misere(l)
                    else:
                        coup, rangee = bot_facile(mode_jeu, coup_max, l)
                    txt_4 = texte(ligne_1 * 5, ligne_2 * 0, f'le bot a pris {coup} de la rangée {rangee + 1}', couleur='white', taille= police_txt, ancrage= 'n')
                    print(f'le bot a joué {coup} dans la rangée {rangee + 1} ')
                    print(l)
                    for i in range(coup):
                        efface(lst[rangee] [len(lst[rangee]) - 1])
                        lst[rangee].pop()
                    attente(2)
                    efface(txt_4)
                elif mode_jeu[0] == 'normal' :
                    attente(1)
                    if diff_bot == 'dur':
                        coup = strategie_normal_misére(nb_objet, coup_max)
                    else:
                        coup = bot_facile(mode_jeu, coup_max, l)
                    txt_2 = texte(ligne_1 * 5, ligne_2 * 2, f'le bot a pris {coup} objet(s)', couleur='white', taille= police_txt, ancrage= 'n')
                    print(f'le bot a joué {coup}')
                    nb_objet -= coup
                    print( f'il reste {nb_objet } objet ')
                    for i in range(coup):
                        efface(lst[len(lst) - 1])
                        lst.pop()
                    attente(2)
                    efface(txt_2)
            else:
                if mode_jeu[0] == 'marienbad' :
                    coup , rangee = jeudujoeuree(taille_fenetre, mode_jeu)
                    while coup_jouer_marienbad(l, coup, rangee) == None:
                        coup , rangee = jeudujoeuree(taille_fenetre, mode_jeu) 
                    for i in range(coup):
                        efface(lst[rangee - 1] [len(lst[rangee - 1]) - 1])
                        lst[rangee - 1 ].pop()
                    print(l)
                elif mode_jeu[0] == 'normal' :
                    coup = jeudujoeuree(taille_fenetre, mode_jeu)
                    while coup_jouer_normal(nb_objet, coup, coup_max) == None:
                        coup = jeudujoeuree(taille_fenetre, mode_jeu)
                    nb_objet -= coup 
                    print( f'il reste {nb_objet } objet ')
                    for i in range(coup):
                        efface(lst[len(lst) - 1])
                        lst.pop()
        if mode_jeu[1] == 'normale':  # mode normale
            gagnant = nb + 1
            if mode_jeu[2] == 'ordi' and gagnant == 2:
                gagnant = '(._.)'
                image(ligne_1 * 5, ligne_2 * 4 ,'bot4.gif', ancrage = 'center')
        else:  # mode misere
            gagnant = (1 - nb) + 1
            if mode_jeu[2] == 'ordi' and gagnant == 2:
                gagnant = '(._.)'
                image(ligne_1 * 5, ligne_2 * 4 ,'bot4.gif', ancrage = 'center')
        if gagnant != '(._.)' :
            image(ligne_1 * 5, ligne_2 * 4 ,'felicitations1.png', ancrage = 'center')
        texte( 5 * ligne_1, ligne_2, f'le gagnant est le joueur {gagnant}', 'white', 'c', 'Helvetica', taille = taille_fenetre[0] // 35)
        
        print(f'le gagnant est le joueur {gagnant}')
        tev = attend_ev()
        if(type_ev(tev ) == 'Return' ) :
            ferme_fenetre()
    ferme_fenetre()