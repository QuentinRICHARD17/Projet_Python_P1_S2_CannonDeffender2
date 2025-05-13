import pygame

class Bateau:
    def __init__(self, position, pv):
        self.position = list(position)
        self.pv = pv

        image_origine = pygame.image.load("ressources/images/BateauSansFond.png")
        largeur = image_origine.get_width() // 2
        hauteur = image_origine.get_height() // 2
        self.image = pygame.transform.scale(image_origine, (largeur, hauteur))

    def avancer(self):
        self.position[0] -= 2

    def afficher(self, surface):
        surface.blit(self.image, self.position)

    def a_touche_chateau(self):
        return self.position[0] <= 25
