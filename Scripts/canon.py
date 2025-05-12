import pygame

class Canon:
    def __init__(self, position, angle, puissance):
        self.angle = angle
        self.puissance = puissance

        image_origine = pygame.image.load("ressources/images/JusteCanon.png")

        largeur = image_origine.get_width() // 3
        hauteur = image_origine.get_height() // 3
        self.image = pygame.transform.scale(image_origine, (largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = self.rect.topleft

    def afficher(self, surface):
        surface.blit(self.image, self.rect.topleft)
