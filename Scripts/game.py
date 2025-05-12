import pygame
from Scripts.canon import Canon
from Scripts.bateau import Bateau
from Scripts.projectile import Boulet
from Scripts.collision import (
    detecter_collisions_boulet_bateau,
    detecter_collisions_chateau_bateau,
    Explosion
)


class Game:
    def __init__(self, fenetre, fond):
        self.fenetre = fenetre
        self.fond = fond
        self.chateau = {"pv": 100}

        self.canon = Canon(position=(80, 210), angle=45, puissance=15)

        self.bateaux = [
            Bateau(position=(1100, 350), pv=30)
        ]

        self.boulets = []
        self.explosions = []

    def lancer(self):
        running = True
        while running:
            self.fenetre.blit(self.fond, (0, 0))

            self.canon.afficher(self.fenetre)

            for bateau in self.bateaux:
                bateau.afficher(self.fenetre)

            for explosion in self.explosions[:]:
                if explosion.est_terminee():
                    self.explosions.remove(explosion)
                else:
                    explosion.afficher(self.fenetre)

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

            detecter_collisions_boulet_bateau(self.boulets, self.bateaux)
            detecter_collisions_chateau_bateau(self.bateaux, self.chateau, self.explosions)

            pygame.display.flip()
