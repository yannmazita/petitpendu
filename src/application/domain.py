from pathlib import Path


class Joueur:
    """Informations d'un joueur du pendu."""

    def __init__(self):
        self.__nom: str = ""
        self.__points: int = 0
        self.__parties: int = 0
        self.__ratioVictoires: float = 1

    @property
    def nom(self):
        """Nom d'un joueur."""
        return self.__nom

    @nom.setter
    def nom(self, nomDuJoueur):
        self.__nom = nomDuJoueur

    @property
    def points(self):
        """Points d'un joueur."""
        return self.__points

    @points.setter
    def points(self, pointsJoueur):
        self.__points = pointsJoueur

    @property
    def parties(self):
        """Nombre de parties du joueur."""
        return self.__parties

    @parties.setter
    def parties(self, partiesJoueur):
        self.__parties = partiesJoueur

    @property
    def ratioVictoires(self):
        """Ratio de victoires du joueur."""
        return self.__ratioVictoires

    @ratioVictoires.setter
    def ratioVictoires(self, ratio):
        self.__ratioVictoires = ratio


class Dictionnaire:
    """Informations sur le dictionnaire de mots"""

    def __init__(self):
        self.__chemin: Path = Path("")
        self.__mot: str = ""

    @property
    def chemin(self):
        """Chemin d'accès du dictionnaire"""
        return self.__chemin

    @chemin.setter
    def chemin(self, cheminAcces):
        self.__chemin = cheminAcces

    @property
    def mot(self):
        """Mot du dictionnaire à trouver"""
        return self.__mot

    @mot.setter
    def mot(self, motDictionnaire):
        self.__mot = motDictionnaire
