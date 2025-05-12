import pygame
from Scripts.game import Game

pygame.init()

LARGEUR, HAUTEUR = 1080, 720
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Canon Defender 2")
fond = pygame.image.load("ressources/images/FondDuJeu.png")
fond = pygame.transform.scale(fond, (LARGEUR, HAUTEUR))
jeu = Game(fenetre, fond)

jeu.lancer()
pygame.quit()