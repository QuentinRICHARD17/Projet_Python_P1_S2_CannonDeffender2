import pygame
pygame.mixer.init()

son_explosion = pygame.mixer.Sound("ressources/Sounds/Explosion_Myinstants.mp3")
son_explosion.set_volume(0.5)  # 0.0 = muet et 1.0 = max
son_game_over = pygame.mixer.Sound("ressources/Sounds/GameOver_Myinstants.mp3")
musique_fond = "ressources/Sounds/MusiqueDeFondPiratesLibreDeDroit.mp3"
son_compte_rebours = pygame.mixer.Sound("ressources/Sounds/3_2_1_Go_Myinstants.mp3")

def jouer_son_explosion():
    son_explosion.play()
def jouer_son_game_over():
    son_game_over.play()

def jouer_musique_de_fond():
    pygame.mixer.music.load(musique_fond)
    pygame.mixer.music.play(-1)  # "-1" fait tourner en boucle

def jouer_compte_rebours():
    son_compte_rebours.play()
