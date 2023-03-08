import sys

from src.application.services import Jeu


class Tui:
    def __init__(self):
        self.__jeu: Jeu = Jeu()

    @property
    def jeu(self):
        """Instance du jeu."""
        return self.__jeu

    def initialisationJoueur(self) -> None:
        """
            Initialisation du joueur entré par l'utilisateur.
        Returns:
            None
        """

        while True:
            sys.stdout.write(f"Quel est le nom du joueur ? : ")
            nom = sys.stdin.readline().strip()
            try:
                nom.encode('ascii')
                break
            except UnicodeEncodeError:
                sys.stdout.write(f"Seuls les caractères ASCII sont autorisés.\n")

        self.__jeu.ajouterJoueurs(nom)

    def afficherInformationsInitiales(self) -> None:
        """
        Affiche les informations initiales du joueur.
        Returns:
            None
        """
        nom: str = self.__jeu.joueur.nom
        points: int = self.__jeu.joueur.points
        parties: int = self.__jeu.joueur.parties
        ratio: float = self.__jeu.joueur.ratioVictoires
        sys.stdout.write(f"{nom}, vous avez actuellement {points} points.\n")
        sys.stdout.write(f"Vous avez gagné {ratio} % des {parties} partie(s) jouée(s).\n")

    def afficherMotCourant(self) -> None:
        """
        Affiche le mot à trouver dans son état de découverte.
        Returns:
            None
        """
        mot: list[str] = self.__jeu.motCourant
        sys.stdout.write(f"{' '.join(mot)}\n")
        #sys.stdout.write(f"{self.__jeu.dico.mot}\n")

    def demanderLettre(self) -> None:
        """
        Demande une lettre au joueur.
        Returns:
            None
        """
        while True:
            sys.stdout.write(f"{self.__jeu.joueur.nom}, donnez une lettre (reste {self.__jeu.essais} essais)\n")
            lettre: str = sys.stdin.readline().strip()
            try:
                self.__jeu.saisieLettre(lettre)
                break
            except TypeError as e:
                sys.stdout.write(f"{e}")

    def afficherStatutPartie(self) -> bool | None:
        """
        Affiche si le joueur a gagné ou perdu la partie.
        Returns:
            bool | None: True si le joueur a gagné False s'il a perdu, None sinon.
        """
        statut: bool | None = self.__jeu.determinerStatutPartie()
        if statut:
            sys.stdout.write(f"Bravo {self.__jeu.joueur.nom}, vous avez trouvé en {self.__jeu.essais} "
                             f"essais le mot : {self.__jeu.dico.mot}\n")
            sys.stdout.write(f"Vous avez gagné {self.__jeu.joueur.points} points\n")
            return True
        elif statut is False:
            sys.stdout.write(f"Perdu!! Vous n'avez pas trouvé en {Jeu.essaisMax} essais\n")
            return False
        elif statut is None:
            return None

    def continuer(self) -> bool:
        """
        Demande au joueur s'il veut continuer de jouer.
        Returns:
            bool: True s'il désire continuer, False sinon.
        """
        sys.stdout.write(f"Voulez-vous continuer [y/n] ? : ")
        choix: str = sys.stdin.readline().strip()
        while choix not in ['y', 'n']:
            sys.stdout.write(f"Seuls 'y' ou 'n' sont autorisés\n")
            choix = sys.stdin.readline().strip()

        if choix == 'y':
            return True
        else:
            return False
