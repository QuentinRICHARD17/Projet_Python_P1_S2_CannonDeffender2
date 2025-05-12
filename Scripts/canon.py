import pygame
from Scripts.projectile import Boulet
import math

class Canon:
    def __init__(self, position, angle, puissance):
        self.position = position
        self.angle = angle
        self.puissance = puissance
        image_origine = pygame.image.load("ressources/images/JusteCanon.png")
        largeur = image_origine.get_width() // 4
        hauteur = image_origine.get_height() // 4
        self.image_originale = pygame.transform.scale(image_origine, (largeur, hauteur))
        self.image = self.image_originale
        self.rect = self.image.get_rect(center=self.position)

    def ajuster_angle(self, variation):
        self.angle = max(-45, min(45, self.angle + variation))

    def tirer(self):
        return Boulet((80, 170), self.angle, self.puissance)

    def afficher(self, surface):
        self.image = pygame.transform.rotate(self.image_originale, -self.angle)
        self.rect = self.image.get_rect(center=self.position)
        surface.blit(self.image, self.rect)
