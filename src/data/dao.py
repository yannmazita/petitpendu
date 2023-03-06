from pathlib import Path
from random import uniform
from unidecode import unidecode
import json

from src.application.domain import Joueur
from src.application.helpers import getProjectRoot


class Dictionnaire:
    """Accès aux données du dictionnaire."""

    @staticmethod
    def recupererMotAleatoire(path: Path) -> str:
        """
        Récupération d'un mot aléatoire dans un dictionnaire.
        Args:
            path: Le chemin du dictionnaire.

        Returns:
            str: Le mot aléatoire.
        """
        numeroLigne: int = 0
        ligneSelect: str = ""
        with open(path) as fichier:
            while True:
                ligne = fichier.readline()
                if not ligne:  # Si la ligne est vide on arrête
                    break
                numeroLigne += 1
                if uniform(0, numeroLigne) < 1:
                    # Lorsqu'on a vu N lignes, la probabilité qu'une ligne soit sélectionnée est 1/N
                    ligneSelect = ligne

        motUnidecode: str = unidecode(ligneSelect.strip(), "utf-8")     # Tout accent est supprimé.
        return motUnidecode


class Save:
    """Accès aux données des sauvegardes."""
    class JoueurSerialisation(json.JSONEncoder):
        """Sérialisation de quelques informations sur le joueur."""
        def default(self, obj):     # Redéfinition de json.JSONEncoder.default() pour les instances de Joueur.
            if isinstance(obj, Joueur):
                data = {
                    "__Joueur__": True,
                    "nom": f"{obj.nom}",
                    "points": f"{obj.points}",
                    "ratio": obj.ratioVictoires,
                    "parties": obj.parties
                }
                return data
            else:
                return super().default(obj)

    @staticmethod
    def joueurDeserialisation(dic: dict) -> Joueur | dict:
        """
        Désérialisation de quelques informations sur le joueur.
        Args:
            dic: Données sérialisées du joueur dans un dictionnaire.

        Returns:
            Joueur | dict: une instance de Joueur ou le dictionnaire lui-même.
        """
        if "__Joueur__" in dic:
            joueur: Joueur = Joueur()
            joueur.nom = dic["nom"]
            joueur.points = dic["points"]
            joueur.ratioVictoires = dic["ratio"]
            joueur.parties = dic["parties"]
            return joueur
        else:
            return dic

    @staticmethod
    def sauvegarderJoueur(joueur: Joueur) -> None:
        """
        Sauvegarde sur le disque de quelques informations sur le joueur.
        Args:
            joueur: Le joueur à sauvegarder.

        Returns:
            None
        """
        with open(Path(getProjectRoot() / "les_exceptions" / "le_pendu" / "sauvegardes" / f"{joueur.nom}.json"), "w") \
                as fichier:
            json.dump(joueur, fichier, indent=4, cls=Save.JoueurSerialisation)

    @staticmethod
    def chargerJoueur(nomJoueur: str) -> Joueur:
        """
        Chargement d'une sauvegarde d'un joueur.
        Args:
            nomJoueur: Le nom du joueur.

        Returns:
            Joueur: Une instance de joueur avec les données chargées.
        """
        with open(Path(getProjectRoot() / "les_exceptions" / "le_pendu" / "sauvegardes" / f"{nomJoueur}.json"), "r") \
                as fichier:
            data = fichier.read()
            return json.loads(data, object_hook=Save.joueurDeserialisation)
