import pygame

class Explosion:
    def __init__(self, position):
        image_origine = pygame.image.load("ressources/images/Explosion.png")
        largeur = image_origine.get_width() // 2
        hauteur = image_origine.get_height() // 2
        self.image = pygame.transform.scale(image_origine, (largeur, hauteur))
        self.position = position
        self.start_time = pygame.time.get_ticks()

    def afficher(self, surface):
        surface.blit(self.image, self.position)

    def est_terminee(self):
        return pygame.time.get_ticks() - self.start_time > 1000


def detecter_collisions_boulet_bateau(boulets, bateaux):
    for boulet in boulets[:]:
        for bateau in bateaux[:]:
            if (int(boulet.position[0]) in range(int(bateau.position[0]), int(bateau.position[0]) + 50) and
                int(boulet.position[1]) in range(int(bateau.position[1]), int(bateau.position[1]) + 50)):
                bateau.pv -= 10
                if bateau.pv <= 0:
                    bateaux.remove(bateau)
                boulets.remove(boulet)
                break


def detecter_collisions_chateau_bateau(bateaux, chateau, explosions):
    for bateau in bateaux[:]:
        if bateau.a_touche_chateau():
            bateaux.remove(bateau)
            chateau["pv"] -= 10
            explosions.append(Explosion(bateau.position.copy()))
