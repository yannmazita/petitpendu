import sys
import re

from src.application.services import Jeu


class Tui:
    def __init__(self):
        self.__jeu: Jeu = Jeu()

    @property
    def jeu(self):
        """Instance du jeu."""
        return self.__jeu

    def initialisationJoueurs(self) -> None:
        """
            Initialisation du nombre de joueurs entré par l'utilisateur.
        Returns:
            None
        """
        print("Combien de joueurs ? : ")
        nombreJoueurs: str = input().strip()

        while not (re.search("^([1-9]|0[1-9]|[1-9]([0-9])+)$", nombreJoueurs)):
            print("Seuls les nombres entiers strictement positifs sont autorisés.\nCombien de joueurs ? : ")
            nombreJoueurs: str = input()

        noms: list[str] = []

        for i in range(0, int(nombreJoueurs)):
            while True:
                print(f"Quel est le nom du joueur {i + 1} ? : ")
                nom = input().strip()
                try:
                    nom.encode('ascii')
                    break
                except UnicodeEncodeError:
                    print(f"Seuls les caractères ASCII sont autorisés.\n")

            noms.append(nom)

        self.__jeu.ajouterJoueurs(noms)

    def afficherInformationsInitiales(self, numeroJoueur: int) -> None:
        """
        Affiche les informations initiales sur un joueur.
        Args:
            numeroJoueur: Le numéro du joueur.

        Returns:
            None
        """
        nom: str = self.__jeu.joueurs[numeroJoueur].nom
        points: int = self.__jeu.joueurs[numeroJoueur].points
        parties: int = self.__jeu.joueurs[numeroJoueur].parties
        ratio: float = self.__jeu.joueurs[numeroJoueur].ratioVictoires
        print(f"{nom}, vous avez actuellement {points} points.\n")
        print(f"Vous avez gagné {ratio} % des {parties} partie(s) jouée(s).\n")

    def afficherMotCourant(self) -> None:
        """
        Affiche le mot à trouver dans son état de découverte.
        Returns:
            None
        """
        mot: list[str] = self.__jeu.motCourant
        print(f"{' '.join(mot)}\n")
        #print(f"{self.__jeu.dico.mot}\n")

    def demanderLettre(self, numeroJoueur: int) -> None:
        """
        Demande une lettre au joueur.
        Args:
            numeroJoueur: Le numéro du joueur.

        Returns:
            None
        """
        while True:
            print(f"Joueur {numeroJoueur}, donnez une lettre (reste {self.__jeu.essais} essais)\n")
            lettre: str = input().strip()
            try:
                self.__jeu.saisieLettre(lettre)
                break
            except TypeError as e:
                print(f"{e}")

    def afficherStatutPartie(self, numeroJoueur: int) -> bool | None:
        """
        Affiche si le joueur a gagné ou perdu la partie.
        Args:
            numeroJoueur: Le numéro du joueur.

        Returns:
            bool | None: True si le joueur a gagné False s'il a perdu, None sinon.
        """
        statut: bool | None = self.__jeu.determinerStatutPartie()
        if statut:
            print(f"Bravo {self.__jeu.joueurs[numeroJoueur].nom}, vous avez trouvé en {self.__jeu.essais} "
                             f"essais le mot : {self.__jeu.dico.mot}\n")
            print(f"Vous avez gagné {self.__jeu.joueurs[numeroJoueur].points} points\n")
            return True
        elif statut is False:
            print(f"Perdu!! Vous n'avez pas trouvé en {self.__jeu.essais} essais\n")
            return False
        elif statut is None:
            return None

    def continuer(self) -> bool:
        """
        Demande au joueur s'il veut continuer de jouer.
        Returns:
            bool: True s'il désire continuer, False sinon.
        """
        print(f"Voulez-vous continuer [y/n] ? : ")
        choix: str = input().strip()
        while choix not in ['y', 'n']:
            print(f"Seuls 'y' ou 'n' sont autorisés\n")
            choix = input().strip()

        if choix == 'y':
            return True
        else:
            return False
