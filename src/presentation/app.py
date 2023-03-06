import sys
from pathlib import Path

from tui import Tui
from src.application.helpers import getProjectRoot


def main() -> int:
    tui: Tui = Tui()

    boucle: bool = True
    while boucle:
        tui.initialisationJoueurs()
        tui.afficherInformationsInitiales(1)
        tui.jeu.recupererMotAleatoire(Path(getProjectRoot() / "french"))

        statut: bool | None = None
        while tui.jeu.essais > 0 and (statut is not True) and (statut is not False):
            for numeroJoueur in tui.jeu.joueurs:
                if tui.jeu.essais > 0 and (statut is not True) and (statut is not False):
                    tui.afficherMotCourant()
                    tui.demanderLettre(numeroJoueur)
                    tui.jeu.calculerPoints(numeroJoueur)
                    statut = tui.afficherStatutPartie(numeroJoueur)
                else:
                    break  # On arrête de parcourir les joueurs quand le jeu se termine.

        tui.jeu.sauvegarderPartie()
        if not tui.continuer():
            boucle = False

    return 0


if __name__ == "__main__":
    sys.exit(main())
