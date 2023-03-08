from pathlib import Path

import src.data.dao as dao
import src.application.domain as domain


class Jeu:
    """
    Informations sur le jeu.

    Attributes:
        essaisMax: Le nombre maximum d'essais.
    """
    essaisMax: int = 8

    def __init__(self):
        self.__joueur: domain.Joueur | None = None
        self.__dico: domain.Dictionnaire = domain.Dictionnaire()
        self.__motCourant: list[str] = []
        self.__positionsCourantes: list[int] = []
        self.__essais: int = Jeu.essaisMax

    @property
    def joueur(self):
        """Joueur du jeu."""
        return self.__joueur

    @property
    def motCourant(self):
        """Mot à trouver dans son état de découverte."""
        return self.__motCourant

    @property
    def dico(self):
        """Dictionnaire"""
        return self.__dico

    @property
    def essais(self):
        """Le nombre d'essais restant."""
        return self.__essais

    @essais.setter
    def essais(self, nombre: int):
        self.__essais = nombre

    @staticmethod
    def chargerJoueur(nomJoueur: str) -> domain.Joueur | None:
        """
        Charge les données sauvegardées d'un joueur s'il existe.
        Args:
            nomJoueur: Le nom du joueur.

        Returns:
            Joueur | None: Une instance de Joueur si le joueur existe, None sinon.
        """
        try:
            joueur: domain.Joueur = dao.Save.chargerJoueur(nomJoueur)
            return joueur
        except IOError:
            return None

    def ajouterJoueurs(self, nom: str) -> None:
        """
        Ajouter un joueur à la collection de Jeu.
        Args:
            nom: Le nom du joueur à ajouter.

        Returns:
            None
        """
        joueur: domain = Jeu.chargerJoueur(nom)
        if joueur is None:
            joueur = domain.Joueur()
            joueur.nom = nom
        self.__joueur = joueur

    def recupererMotAleatoire(self, path: Path) -> None:
        """
        Récupère un mot aléatoire dans un dictionnaire.
        Args:
            path: Le chemin du dictionnaire.

        Returns:
            None
        """
        self.__dico.mot = dao.Dictionnaire.recupererMotAleatoire(path)
        self.__motCourant = ['*' for _ in range(0, len(self.__dico.mot))]

    def determinerMotCourant(self) -> None:
        """
        Détermine le mot courant à partir de self.__positionCourantes.
        Returns:
            None
        """
        for i in self.__positionsCourantes:
            self.__motCourant[i] = self.__dico.mot[i]

    def saisieLettre(self, lettre: str) -> None:
        """
        Construction du mot à trouver ainsi que la position des lettres trouvées à partir d'une lettre saisie.
        Args:
            lettre: La lettre saisie par le joueur.

        Returns:
            None
        """
        if lettre.isascii() and lettre.isalpha():
            self.__positionsCourantes = [pos for pos, car in enumerate(self.__dico.mot) if car == lettre]
            try:
                self.determinerMotCourant()
            except IndexError:
                pass
        elif lettre == "":
            pass
        else:
            raise TypeError("Seules les lettres sont autorisées")

    def calculerPoints(self) -> None:
        """
        Calcul de différents points du jeu.
        Returns:
            None
        """
        if not self.__positionsCourantes:
            self.__essais = max(0, self.__essais - 1)

        if "".join(self.__motCourant) == self.__dico.mot:
            self.__joueur.points += self.__essais
        if self.__essais == 0:
            pointsCourants: int = self.__joueur.points
            self.__joueur.points = max(0, pointsCourants - 3)

    def determinerStatutPartie(self) -> bool | None:
        """
        Détermine si la partie a été gagnée ou perdue. Augmente le nombre de parties et victoires en conséquence.
        Returns:
            bool: True si la partie est gagnée, False si perdue, None sinon.
        """
        if self.__essais == 0:
            self.__joueur.parties += 1
            return False
        elif "".join(self.__motCourant) == self.__dico.mot:
            self.__joueur.parties += 1
            self.__joueur.victoires += 1
            return True
        return None

    def sauvegarderPartie(self) -> None:
        """
        Sauvegarde des informations du joueur de la partie.
        Returns:
            None
        """
        dao.Save.sauvegarderJoueur(self.__joueur)
