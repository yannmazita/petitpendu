import sys
from pathlib import Path

from src.presentation.tui import Tui
from src.application.helpers import getProjectRoot


def main() -> int:
    boucle: bool = True
    while boucle:
        try:
            tui: Tui = Tui()
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
        except Exception:
            print("Données du jeu")
            print(f"joueurs={tui.jeu.joueurs}")
            print(f"joueurs={tui.jeu.dico}")
            print(f"essais={tui.jeu.essais}")
            print(f"Données des joueurs")
            for i in tui.jeu.joueurs:
                print(f"nom={tui.jeu.joueurs[i].nom}")
                print(f"points={tui.jeu.joueurs[i].points}")
                print(f"parties={tui.jeu.joueurs[i].parties}")
                print(f"ratioVictoires={tui.jeu.joueurs[i].ratioVictoires}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
