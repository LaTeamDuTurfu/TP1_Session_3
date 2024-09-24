from Controllers import Database
from Models import *
from ModuleUtilitaire.utilpy.Console.console_utils import *


class Catalogue:
    def __init__(self, database: Database):
        self.database = database

    def ajouter_partie(self):
        # Heading
        print("------ Ajouter une partie -----\n")

        # Création des joueurs
        joueur1_nom = lire_chaine("Entrez le nom du joueur 1: ")
        joueur1_niveau = lire_entier("Entrez l'Elo du joueur 1:")
        joueur2_nom = lire_chaine("Entrez le nom du joueur 2: ")
        joueur2_niveau = lire_entier("Entrez l'Elo du joueur 2:")
        joueur1 = Joueur(joueur1_nom, joueur1_niveau)
        joueur2 = Joueur(joueur2_nom, joueur2_niveau)

        # Spécifitiés de la partie
        date = lire_date("Entrez la date à laquelle la date a été jouée (DD-MM-AAAA): ")
        type = lire_caractère("Quel est le type de la partie: ")
        durée = lire_entier("Entrez la durée de la partie en minutes: ")
        résultat = lire_entier_intervalle(f"Est-ce {joueur1_nom} [1] qui à gagné ou {joueur2_nom} [2]: ")
        ouverture = lire_caractère("Quelle était l'ouverture utilisée: ")
        moves = input("Écrivez les moves dans un format PGN: ")

        # Création de la partie
        nouvelle_partie = Partie(joueur1, joueur2, date, type, durée, résultat, ouverture, moves)

        # Ajout partie dans la base de donnée
        self.database.parties.append(nouvelle_partie)

    def display_parties(self):
        for index_partie, partie_jouée in enumerate(self.database.parties):
            print(f"[{index_partie + 1}] {partie_jouée}")

    def modifier_partie(self):
        pass

    def supprimer_partie(self):
        pass
