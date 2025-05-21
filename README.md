# Canon Defender

Petit jeu en Python avec Pygame où tu dois défendre ton château contre des bateaux ennemis en utilisant un canon.

## Comment jouer

- Lance le fichier `Main.py`
- Clique sur **Jouer** à l’écran d’accueil
- Utilise les **flèches haut et bas** pour bouger l’angle du canon
- Appuie sur **Espace** pour tirer un boulet
- Les bateaux avancent vers ton château, détruis-les avant qu’ils ne l’atteignent
- Si le château perd tous ses points de vie, c’est game over

## Organisation des fichiers

- **`Projet_Python_P1_S2_CannonDeffender2/`** : Dossier racine du projet.
    - **`Main.py`** : # Menu d'accueil et lancement du jeu
    - **`ressources/`** : Dossier contenant les ressources graphiques et sonores.
        - **`images/`** : # Contient les images du jeu.
            - `BateauCoule.png`
            - `BateauSansFond.png`
            - `BouletDeCanon.png`
            - `Explosion.png`
            - `Fond_Ocean_et_ciel.png`
            - `FondDuJeu.png`
            - `FondPageAccueil.png`
            - `FondPageGameOver.png`
            - `JusteCanon.png`
        - **`Sounds/`** : # Contient les effets sonores et musiques du jeu.
            - `3_2_1_Go_MyInstants.mp3`
            - `Explosion_MyInstants.mp3`
            - `GameOver_MyInstants.mp3`
            - `MusiqueDeFondPiratesLibreDeDroit.mp3`
    - **`Scripts/`** : Dossier contenant les scripts Python du jeu.
        - **`game.py`** : # Logique principale du jeu
        - **`canon.py`** : # Gestion du canon
        - **`bateau.py`** : # Gestion des bateaux ennemis
        - **`projectile.py`** : # Gestion des boulets
        - **`collision.py`** : # Détection des collisions et explosions
        - **`interface.py`** : # Affichage des infos (PV, score, vague)
        - **`sons.py`** : # Gestion des sons du jeu (musique, effets)

## Pré-requis

Avant de lancer le jeu, assure-toi d'avoir :

- Python 3 installé
- Le module `pygame` installé

Pour installer pygame :

```bash
pip install pygame
```

## Aperçu du jeu 

![FondPageAccueil.png](ressources%2Fimages%2FFondPageAccueil.png)