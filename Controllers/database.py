from Models import *
import os


class Database:
    def __init__(self):
        self.parties = []
        self.folder_path = '../Data'

    def load_parties(self):
        for file in os.listdir(self.folder_path):
            if file.endswith('.pgn'):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r') as f:
                    joueur1 = f.readline()
                    joueur2 = f.readline()
                    date = f.readline()
                    type_partie = f.readline()
                    durée = f.readline()
                    résultat = f.readline()
                    ouverture = f.readline()
                    moves = f.readline()
                    nouvelle_partie = Partie(joueur1, joueur2, date, type_partie, durée, résultat, ouverture, moves)
                    self.parties.append(nouvelle_partie)



    def save_parties(self):
        pass


db = Database()
db.load_parties()
for partie in db.parties:
    print(partie)