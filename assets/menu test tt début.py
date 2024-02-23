import pygame
import sys

pygame.init()

# Initialise la fenêtre
fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ratz Fighter")  # Titre de la fenetre 

# Charge l'image du titre et musique
titre_img = pygame.image.load("assets/Titre RATZ FIGHTER.png")
titre_img = pygame.transform.scale(titre_img, (1300, 500))
pygame.mixer.music.load("assets/intro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(5000)

jeu_en_cours = True  # Variable pour contrôler la boucle principale

def Menu():
    global jeu_en_cours  # Rendre la variable jeu_en_cours accessible dans la fonction

    while jeu_en_cours:
        for event in pygame.event.get():
            # Quitter le jeu si l'utilisateur clique sur la croix
            if event.type == pygame.QUIT:
                jeu_en_cours = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    if exit_button.collidepoint(event.pos):
                        jeu_en_cours = False  # Quitter le jeu

        # Afficher l'image du titre au centre de l'écran
        x = (800 - titre_img.get_width()) // 2 + 20
        y = (600 - titre_img.get_height()) // 2 - 80  # POUR BOUGER IMPORTANT
        fenetre.blit(titre_img, (x, y))

        # Création et affichage des boutons
        # Bouton Play
        play_button = pygame.Rect(250, 250, 300, 100)
        play_text = pygame.font.Font("assets/font.ttf", 40).render("Play", True, (255, 255, 255))
        fenetre.blit(play_text, (300, 255))

        # Bouton Options
        options_button = pygame.Rect(250, 350, 300, 100)
        options_text = pygame.font.Font("assets/font.ttf", 40).render("Options", True, (255, 255, 255))
        fenetre.blit(options_text, (250, 355))

        # Bouton Exit
        exit_button = pygame.Rect(250, 450, 300, 100)
        exit_text = pygame.font.Font("assets/font.ttf", 40).render("Quitter", True, (255, 255, 255))
        fenetre.blit(exit_text, (250, 455))

        # Mettre à jour l'écran
        pygame.display.flip()

Menu()
pygame.quit()
sys.exit()
