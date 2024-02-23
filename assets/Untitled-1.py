import pygame
import sys

pygame.init()

# Initialise la fenêtre
fenetre = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Ratz Fighter")  # Titre de la fenetre 

# Charge l'image du titre et musique
titre_img = pygame.image.load("assets/Titre RATZ FIGHTER.png")
titre_img = pygame.transform.scale(titre_img, (1300, 500))
pygame.mixer.music.load("assets/intro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(5000)

jeu_en_cours = True  # Variable pour contrôler la boucle principale

def Options():
    global jeu_en_cours

    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.collidepoint(event.pos):
                        return  # Retourner au menu principal

        fenetre.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

        # Afficher le titre du menu Options
        options_title = pygame.font.Font("assets/font.ttf", 60).render("Options", True, (255, 255, 255))
        x = (800 - options_title.get_width()) // 2
        y = 50
        fenetre.blit(options_title, (x, y))

        # Bouton de retour
        back_button = pygame.Rect(20, 20, 100, 50)
        back_text = pygame.font.Font("assets/font.ttf", 30).render("Retour", True, (255, 255, 255))
        fenetre.blit(back_text, (30, 30))

        # Ajouter des options ici


        pygame.display.flip()

# Modifie la fonction Menu pour ajouter la gestion du bouton Options
def Menu():
    global jeu_en_cours

    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_button.collidepoint(event.pos):
                        print("Lancer le jeu")  # Ajoute ici la logique pour lancer le jeu
                    elif options_button.collidepoint(event.pos):
                        Options()  # Appeler la fonction Options
                    elif exit_button.collidepoint(event.pos):
                        jeu_en_cours = False

        fenetre.fill((0, 0, 0))

        x = (800 - titre_img.get_width()) // 2 + 20
        y = (600 - titre_img.get_height()) // 2 - 80
        fenetre.blit(titre_img, (x, y))

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

        pygame.display.flip()

Menu()
pygame.quit()
sys.exit()
