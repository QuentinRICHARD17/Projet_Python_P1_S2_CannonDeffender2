import pygame
from Scripts.canon import Canon
from Scripts.bateau import Bateau
from Scripts.projectile import Boulet
from Scripts.collision import *
from Scripts.interface import Interface
from Scripts.sons import *



class Game:
    def __init__(self, fenetre, fond):
        self.fenetre = fenetre
        self.fond = fond
        self.chateau = {"pv": 100}
        self.canon = Canon(position=(80, 210), angle=0, puissance=400)
        self.bateaux = [Bateau(position=(1100, 350), pv=30)]
        self.boulets = []
        self.explosions = []
        self.bateaux_coules = []
        self.temps_derniere_generation = pygame.time.get_ticks()
        self.temps_dernier_tir = 0
        self.delai_tir = 1000
        self.bateaux_tues = 0
        self.vague = 1
        self.police = pygame.font.Font(None, 36)
        self.interface = Interface(self.police)

    def lancer(self):
        jouer_compte_rebours()
        pygame.time.wait(3000)
        jouer_musique_de_fond()
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

            for bateau_coule in self.bateaux_coules[:]:
                if bateau_coule.est_termine():
                    self.bateaux_coules.remove(bateau_coule)
                else:
                    bateau_coule.afficher(self.fenetre)

            for boulet in self.boulets:
                boulet.deplacement()
                boulet.afficher(self.fenetre)

            self.interface.afficher_infos(self.fenetre, self.chateau["pv"], self.bateaux_tues, self.vague)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        maintenant = pygame.time.get_ticks()
                        if maintenant - self.temps_dernier_tir >= self.delai_tir:
                            boulet = self.canon.tirer()
                            self.boulets.append(boulet)
                            self.temps_dernier_tir = maintenant
                    elif event.key == pygame.K_UP:
                        self.canon.ajuster_angle(-5)
                    elif event.key == pygame.K_DOWN:
                        self.canon.ajuster_angle(5)

            for bateau in self.bateaux:
                bateau.avancer()

            nb_avant = len(self.bateaux)
            detecter_collisions_boulet_bateau(self.boulets, self.bateaux, self.explosions, self.bateaux_coules)
            nb_tues = nb_avant - len(self.bateaux)
            self.bateaux_tues += nb_tues

            detecter_collisions_chateau_bateau(self.bateaux, self.chateau, self.explosions)

            if self.chateau["pv"] <= 0:
                self.afficher_game_over()
                running = False

            if self.bateaux_tues >= self.vague * 10:
                self.vague += 1
                for bateau in self.bateaux:
                    bateau.pv += 10

            temps_actuel = pygame.time.get_ticks()
            if temps_actuel - self.temps_derniere_generation >= 10000:
                pv_bateau = 30 + self.vague * 10
                self.bateaux.append(Bateau(position=(1100, 350), pv=pv_bateau))
                self.temps_derniere_generation = temps_actuel

            pygame.display.flip()

    def afficher_game_over(self):
        fond_game_over = pygame.image.load("ressources/images/FondPageGameOver.png")
        jouer_son_game_over()
        fond_game_over = pygame.transform.scale(fond_game_over, (self.fenetre.get_width(), self.fenetre.get_height()))
        self.fenetre.blit(fond_game_over, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)
