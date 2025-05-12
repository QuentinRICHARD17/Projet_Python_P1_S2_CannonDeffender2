import pygame
from Scripts.canon import Canon
from Scripts.bateau import Bateau
from Scripts.projectile import Boulet
from Scripts.collision import (
    detecter_collisions_boulet_bateau,
    detecter_collisions_chateau_bateau,
    Explosion
)
from Scripts.interface import Interface


class Game:
    def __init__(self, fenetre, fond):
        self.fenetre = fenetre
        self.fond = fond
        self.chateau = {"pv": 100}
        self.canon = Canon(position=(80, 210), angle=45, puissance=15)
        self.bateaux = [Bateau(position=(1100, 350), pv=30)]
        self.boulets = []
        self.explosions = []
        self.temps_derniere_generation = pygame.time.get_ticks()
        self.bateaux_tues = 0
        self.vague = 1
        self.police = pygame.font.Font(None, 36)
        self.interface = Interface(self.police)

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

            self.interface.afficher_infos(self.fenetre, self.chateau["pv"], self.bateaux_tues, self.vague)

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

            nb_avant = len(self.bateaux)
            detecter_collisions_boulet_bateau(self.boulets, self.bateaux)
            self.bateaux_tues += nb_avant - len(self.bateaux)

            detecter_collisions_chateau_bateau(self.bateaux, self.chateau, self.explosions)

            temps_actuel = pygame.time.get_ticks()
            if temps_actuel - self.temps_derniere_generation >= 10000:
                self.bateaux.append(Bateau(position=(1100, 350), pv=30))
                self.temps_derniere_generation = temps_actuel

            pygame.display.flip()
