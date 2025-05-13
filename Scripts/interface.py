import pygame

class Interface:
    def __init__(self, police):
        self.police = police

    def afficher_infos(self, surface, pv_chateau, nb_bateaux_tues, vague):
        texte_pv = self.police.render(f"Château : {pv_chateau} PV", True, (0, 0, 0))
        texte_vague = self.police.render(f"Vague : {vague}", True, (0, 0, 0))
        texte_pv_bateaux = self.police.render(f"PV bateaux : {30 + vague * 10}", True, (0, 0, 0))
        texte_score = self.police.render(f"Bateaux coulés : {nb_bateaux_tues}", True, (0, 0, 0))

        surface.blit(texte_pv, (20, 20))
        surface.blit(texte_vague, (20, 50))
        surface.blit(texte_pv_bateaux, (20, 80))
        surface.blit(texte_score, (20, 110))
