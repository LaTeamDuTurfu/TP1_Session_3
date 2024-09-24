from Controllers import Database
from Models import *
from ModuleUtilitaire.utilpy.Console.console_utils import *


class Catalogue:
    def __init__(self, database: Database):
        self.database = database

    def ajouter_partie(self):
        # Heading
        print("------ Ajouter une partie -----")

        # Création des joueurs
        joueur1_nom = lire_chaine("Entrez le nom du joueur 1: ")
        joueur1_niveau = lire_entier("Entrez l'Elo du joueur 1:")
        joueur2_nom = lire_chaine("Entrez le nom du joueur 2: ")
        joueur2_niveau = lire_entier("Entrez l'Elo du joueur 2:")
        joueur1 = Joueur(joueur1_nom, joueur1_niveau)
        joueur2 = Joueur(joueur2_nom, joueur2_niveau)

        #

    def modifier_partie(self):
        pass

    def supprimer_partie(self):
        pass
