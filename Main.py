import pygame
from Scripts.game import Game

def afficher_accueil(fenetre, largeur, hauteur):
    fond = pygame.image.load("ressources/images/FondPageAccueil.png")
    fond = pygame.transform.scale(fond, (largeur, hauteur))

    police = pygame.font.Font(None, 50)
    texte_bouton = police.render("Jouer", True, (255, 255, 255))

    bouton_rect = pygame.Rect(440, 550, 200, 60)

    en_attente = True
    while en_attente:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rect.collidepoint(evenement.pos):
                    en_attente = False

        fenetre.blit(fond, (0, 0))
        pygame.draw.rect(fenetre, (0, 120, 200), bouton_rect, border_radius=10)
        fenetre.blit(texte_bouton, texte_bouton.get_rect(center=bouton_rect.center))
        pygame.display.flip()


def lancer_jeu():
    pygame.init()
    LARGEUR, HAUTEUR = 1080, 720
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

    afficher_accueil(fenetre, LARGEUR, HAUTEUR)

    fond_jeu = pygame.image.load("ressources/images/FondDuJeu.png")
    fond_jeu = pygame.transform.scale(fond_jeu, (LARGEUR, HAUTEUR))

    jeu = Game(fenetre, fond_jeu)
    jeu.lancer()
    pygame.quit()


if __name__ == "__main__":
    lancer_jeu()