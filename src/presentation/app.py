import sys
from pathlib import Path

from src.presentation.tui import Tui
from src.application.helpers import getProjectRoot


def main() -> int:
    boucle: bool = True
    while boucle:
        tui: Tui = Tui()
        tui.initialisationJoueur()
        tui.afficherInformationsInitiales()
        tui.jeu.recupererMotAleatoire(Path(getProjectRoot() / "french"))

        statut: bool | None = None
        while tui.jeu.essais > 0 and (statut is not True) and (statut is not False):
            tui.afficherMotCourant()
            tui.demanderLettre()
            tui.jeu.calculerPoints()
            statut = tui.afficherStatutPartie()

        tui.jeu.sauvegarderPartie()
        if not tui.continuer():
            boucle = False

    return 0


if __name__ == "__main__":
    sys.exit(main())
