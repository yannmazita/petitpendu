from pathlib import Path


class Joueur:
    """Informations d'un joueur du pendu."""

    def __init__(self):
        self.__nom: str = ""
        self.__points: int = 0
        self.__parties: int = 0
        self.__victoires: int = 0

    @property
    def nom(self) -> str:
        """Nom d'un joueur."""
        return self.__nom

    @nom.setter
    def nom(self, nomDuJoueur: str) -> None:
        self.__nom = nomDuJoueur

    @property
    def points(self) -> int:
        """Points d'un joueur."""
        return self.__points

    @points.setter
    def points(self, pointsJoueur: int) -> None:
        self.__points = pointsJoueur

    @property
    def parties(self) -> int:
        """Nombre de parties du joueur."""
        return self.__parties

    @parties.setter
    def parties(self, partiesJoueur: int) -> None:
        self.__parties = partiesJoueur

    @property
    def victoires(self) -> int:
        """Nombre de victoires du joueur."""
        return self.__victoires

    @victoires.setter
    def victoires(self, victoiresJoueur: int) -> None:
        self.__victoires = victoiresJoueur


class Dictionnaire:
    """Informations sur le dictionnaire de mots"""

    def __init__(self):
        self.__chemin: Path = Path("")
        self.__mot: str = ""

    @property
    def chemin(self) -> Path:
        """Chemin d'accès du dictionnaire"""
        return self.__chemin

    @chemin.setter
    def chemin(self, cheminAcces: Path) -> None:
        self.__chemin = cheminAcces

    @property
    def mot(self):
        """Mot du dictionnaire à trouver"""
        return self.__mot

    @mot.setter
    def mot(self, motDictionnaire: str) -> None:
        self.__mot = motDictionnaire
