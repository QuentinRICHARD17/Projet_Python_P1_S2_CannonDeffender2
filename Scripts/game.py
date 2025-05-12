import pygame
from Scripts.canon import Canon
from Scripts.bateau import Bateau
from Scripts.projectile import Boulet
from Scripts.collision import detecter_collisions

class Game:
    def __init__(self, fenetre, fond):
        self.fenetre = fenetre
        self.fond = fond
        self.chateau = {"pv": 100}
        self.canon = Canon(position=(100, 650), angle=45, puissance=15)
        self.bateaux = [Bateau(position=(1000, 650), pv=30), Bateau(position=(1150, 670), pv=40)]
        self.boulets = []

    def lancer(self):
        running = True
        while running:
            self.fenetre.blit(self.fond, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        boulet = self.canon.tirer()
                        self.boulets.append(boulet)

            for bateau in self.bateaux:
                bateau.avancer()

            for boulet in self.boulets:
                boulet.deplacement()

            detecter_collisions(self.boulets, self.bateaux)

            pygame.display.flip()