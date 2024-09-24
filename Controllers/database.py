from Models import *
import os


class Database:
    def __init__(self):
        self.parties = []
        self.folder_path = 'Data'

    def load_parties(self):
        for file in os.listdir(self.folder_path):
            if file.endswith('.pgn'):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r') as f:
                    nouvelle_partie = Partie()
                    nouvelle_partie.joueur1 = f.readline()
                    nouvelle_partie.joueur2 = f.readline()
                    nouvelle_partie.date = f.readline()
                    nouvelle_partie.type_partie = f.readline()
                    nouvelle_partie.durée = f.readline()
                    nouvelle_partie.résultat = f.readline()
                    nouvelle_partie.ouverture = f.readline()
                    nouvelle_partie.moves = f.readline()
                    self.parties.append(nouvelle_partie)



    def save_parties(self):
        pass


db = Database()
db.load_parties()
for partie in db.parties:
    print(partie)