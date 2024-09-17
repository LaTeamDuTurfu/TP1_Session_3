class Partie:
    def __init__(self, joueur1, joueur2, date, niveau_j1, niveau_j2, type_partie, durée, résultat, ouverture):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.date = date
        self.niveau_j1 = niveau_j1
        self.niveau_j2 = niveau_j2
        self.type_partie = type_partie
        self.durée = durée
        self.résultat = résultat
        self.ouverture = ouverture

    def __str__(self):
        return f"{self.joueur1} vs {self.joueur2} | {self.type_partie} | {self.date}"

    def __repr__(self):
        self.__str__()
