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


class BateauCouleTemporaire:
    def __init__(self, position, taille):
        image = pygame.image.load("ressources/images/BateauCoule.png")
        self.image = pygame.transform.scale(image, taille)
        self.position = position
        self.temps_depart = pygame.time.get_ticks()

    def afficher(self, surface):
        surface.blit(self.image, self.position)

    def est_termine(self):
        return pygame.time.get_ticks() - self.temps_depart > 1000


def detecter_collisions_boulet_bateau(boulets, bateaux, explosions, bateaux_coules):
    for boulet in boulets[:]:
        rect_boulet = pygame.Rect(boulet.position[0], boulet.position[1],
                                  boulet.image.get_width(), boulet.image.get_height())
        for bateau in bateaux[:]:
            rect_bateau = pygame.Rect(bateau.position[0], bateau.position[1],
                                      bateau.image.get_width(), bateau.image.get_height())

            if rect_boulet.colliderect(rect_bateau):
                explosions.append(Explosion(boulet.position.copy()))
                bateau.pv -= 10

                if bateau.pv <= 0:
                    taille = (bateau.image.get_width(), bateau.image.get_height())
                    bateau_coule = BateauCouleTemporaire(bateau.position.copy(), taille)
                    bateaux_coules.append(bateau_coule)
                    bateaux.remove(bateau)

                boulets.remove(boulet)
                break


def detecter_collisions_chateau_bateau(bateaux, chateau, explosions):
    for bateau in bateaux[:]:
        if bateau.a_touche_chateau():
            bateaux.remove(bateau)
            chateau["pv"] -= 10
            explosions.append(Explosion(bateau.position.copy()))
