import pygame
import math

class Boulet:
    def __init__(self, position, angle_deg, vitesse):
        self.x0, self.y0 = position
        self.angle_rad = math.radians(-angle_deg)
        self.vitesse = vitesse
        self.vx = vitesse * math.cos(self.angle_rad)
        self.vy_initial = -vitesse * math.sin(self.angle_rad)
        self.g = 300
        self.temps = 0
        image_origine = pygame.image.load("ressources/images/BouletDeCanon.png")
        largeur = image_origine.get_width() // 7
        hauteur = image_origine.get_height() // 7
        self.image = pygame.transform.scale(image_origine, (largeur, hauteur))
        self.position = [self.x0, self.y0]

    def deplacement(self):
        self.temps += 0.05
        x = self.x0 + self.vx * self.temps
        y = self.y0 + self.vy_initial * self.temps + 0.5 * self.g * self.temps ** 2
        self.position = [x, y]

    def afficher(self, surface):
        surface.blit(self.image, self.position)
