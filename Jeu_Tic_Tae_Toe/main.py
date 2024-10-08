import pygame
import sys

class Grille:
    def __init__(self,ecran):
        """
        initie la grille
        :param ecran:
        """
        self.ecran = ecran
        self.lignes = [( (200,0),(200,600)),
                       ((400,0),(400,600)),
                       ((0,200),(600,200)),
                       ((0,400),(600,400)),]
        # initier la grille
        self.grille = [[None for x in range(0,3)] for x in range(0,3)]
        #initier la variable pour vérifier si le compteur est 'ON'
        self.compteur_on = False
    def afficher(self):
        """

        Affiche la grille et les X/0

        """
        for ligne in self.lignes:
            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)

   #afficher les X et les O
        for y in range(0,len(self.grille)):
            for x in range(0, len(self.grille)):
                if self.grille[y][x] == 'X':
                    pygame.draw.line(self.ecran, (0,0,0), (x * 200, y * 200), (200 + (x *200), 200 + (y * 200)), 3)
                    pygame.draw.line(self.ecran, (0,0,0), ((x * 200), 200 +(y * 200)),(200 + (x * 200), (y * 200)), 3)

                elif self.grille[y][x] == 'O':

                    pygame.draw.circle(self.ecran, (0, 0, 0), (100 + (x * 200), 100 + ( y * 200)), 100, 3)


# print la grille
    def print_grille(self):
        """

        Afficher la grille dans la console
        """
        print(self.grille)

    def fixer_la_valeur(self,x,y,valeur):

        """
        Fixe la valeur d'une case dans la grille
        :param x:
        :param y:
        :param valeur:
        """
        # condition si une case possède la valeur None
        if self.grille[y][x] == None :
            self.grille[y][x] = valeur
            #Le compteur est ON
            self.compteur_on = True

    # creer une fonction qui fixe la valeur des cases a None

    def fixer_None(self,ligne,colonne,valeur):

        self.grille[ligne][colonne] = valeur

class Jeu :

    def __init__(self):
        self.ecran = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Tic Tae Toe')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)
        # fixer les variables 'X' et 'O'
        self.player_X = 'X'
        self.player_O = 'O'

        # fixer le compteur
        self.compteur = 0

        self.ecran_debut = True

    def fonction_principale(self):

        while self.jeu_encours:

            while self.ecran_debut:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ecran_debut = False


                self.ecran.fill((230,230,230))

                self.creer_message('grande', 'Tic Tac Toe', (0, 0, 0), [200, 30, 200, 50])
                self.creer_message('petite', "Ce jeu se joue à deux et chaqu'un se verra attribuer un symbole ",
                                   (0, 0, 0),
                                   [50, 130, 400, 50])
                self.creer_message('petite', 'X ou O', (0, 0, 0), [220, 150, 100, 100])
                self.creer_message('petite', 'Le premier joueur qui reussi à aligner 3 de ses symboles gagne',
                                   (0, 0, 0), [50, 170, 200, 50])
                self.creer_message('moyenne', 'Pour recommencer le jeu , appuyer sur Enter', (0, 0, 0),
                                   [70, 350, 200, 50])
                self.creer_message('moyenne', 'Appuyer sur Espace pour commencer le jeu ', (0, 0, 0),
                                   [70, 400, 200, 50])
                self.creer_message('moyenne', 'Pour revenir a cette ecran , appuyer sur ESC ', (0, 0, 0),
                                   [70, 450, 200, 50])
                pygame.display.flip()


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                #Ajouter l'évenement qui correspond au clique droit
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:

                    #obtenir la position de la souris
                    position = pygame.mouse.get_pos()

                    position_x, position_y = position[0]//200 ,position[1]//200

                    # condition si le compteur est pair ou impaire
                    if self.compteur %2 == 0:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_X)
                    else:
                        self.grille.fixer_la_valeur(position_x, position_y,self.player_O)
                    #condition si le compteur ON est vrai
                    if self.grille.compteur_on:
                        self.compteur += 1
                    # fixe le compteur ON = Faux
                        self.grille.compteur_on = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.recommencer()

                    if event.key == pygame.K_ESCAPE:
                        self.ecran_debut = True


            liste_X = []
            liste_O = []
            liste_lignes_X = []
            liste_colonnes_X = []
            liste_lignes_O = []
            liste_colonnes_O = []
            self.gagnant(liste_X,liste_O,liste_colonnes_X,liste_lignes_X,liste_lignes_O,liste_colonnes_O)
            self.ecran.fill((240,240,240))
            self.grille.afficher()
            pygame.display.flip()

    def recommencer(self):
        for ligne in range(0, len(self.grille.grille)):
            for colonne in range(0, len(self.grille.grille)):
                self.grille.fixer_None(ligne,colonne,None)

    def creer_message(self,font,message,couleur,message_rectangle):

        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)

        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,False,couleur)

        self.ecran.blit(message,message_rectangle)




    def gagnant(self,liste_X,liste_O,liste_colonnes_X,liste_lignes_X,liste_lignes_O,liste_colonnes_O):



            #print(self.compteur)
            #self.grille.print_grille()

            for ligne in range(0, len(self.grille.grille)):
                for colonne in range(0, len(self.grille.grille)):

                    if self.grille.grille[ligne][colonne] == 'X':
                        X_position = (ligne,colonne)
                        liste_X.append(X_position)

                    elif self.grille.grille[ligne][colonne] == '0':
                        O_position = (ligne,colonne)
                        liste_O.append(O_position)


            if len(liste_X) >= 3:
                for (ligne,colonne) in liste_X:
                    liste_lignes_X.append(ligne)
                    liste_colonnes_X.append(colonne)

                if liste_lignes_X.count(0) == 3 or liste_lignes_X.count(1) == 3 or liste_lignes_X.count(2) == 3:
                    print('X Gagne')

                if liste_colonnes_X.count(0) == 3 or liste_colonnes_X.count(1) == 3 or liste_colonnes_X.count(2) == 3 :
                    print('X Gagne')

                if liste_lignes_X == liste_colonnes_X or liste_lignes_X == liste_colonnes_X[::-1]:
                    print('X Gagne')

                print(liste_lignes_X, liste_colonnes_X)


            if len(liste_O) >= 3:
                for (ligne,colonne) in liste_O:
                    liste_lignes_O.append(ligne)
                    liste_colonnes_O.append(colonne)

                if liste_lignes_O.count(0) == 3 or liste_lignes_O.count(1) == 3 or liste_lignes_O.count(2) == 3:
                    print('O Gagne')

                if liste_colonnes_O.count(0) == 3 or liste_colonnes_O.count(1) == 3 or liste_colonnes_O.count(2) == 3:
                    print('O Gagne')

                if liste_lignes_O == liste_colonnes_O or liste_lignes_O == liste_colonnes_O[::-1]:
                    print('O Gagne')


if __name__ == '__main__':

    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()





