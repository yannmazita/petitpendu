import sys
from pathlib import Path

from src.presentation.tui import Tui
from src.application.helpers import getProjectRoot


def main() -> int:
    boucle: bool = True
    while boucle:
        try:
            tui: Tui = Tui()
            tui.initialisationJoueur()
            tui.afficherInformationsInitiales()
            tui.jeu.recupererMotAleatoire(Path(getProjectRoot() / "french"))

            statut: bool | None = None
            while tui.jeu.essais > 0 and (statut is not True) and (statut is not False):
                if tui.jeu.essais > 0 and (statut is not True) and (statut is not False):
                    tui.afficherMotCourant()
                    tui.demanderLettre()
                    tui.jeu.calculerPoints()
                    statut = tui.afficherStatutPartie()

            tui.jeu.sauvegarderPartie()
            if not tui.continuer():
                boucle = False

        except Exception as e:
            print(e)
            print("Données du jeu")
            print(f"joueurs={tui.jeu.joueur}")
            print(f"joueurs={tui.jeu.dico}")
            print(f"essais={tui.jeu.essais}")

            print(f"Données des joueurs")
            print(f"nom={tui.jeu.joueur.nom}")
            print(f"points={tui.jeu.joueur.points}")
            print(f"parties={tui.jeu.joueur.parties}")
            print(f"ratioVictoires={tui.jeu.joueur.ratioVictoires}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
