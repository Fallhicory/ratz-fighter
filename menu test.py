import pygame
import sys

pygame.init()
pygame.joystick.init()  # module pour manettes
larg_ecran = 800
long_ecran = 600
# Initialise la fenêtre
fenetre = pygame.display.set_mode((larg_ecran, long_ecran))
pygame.display.set_caption("Ratz Fighter")  # Titre de la fenetre

# Charge l'image du titre et musique
titre_img = pygame.image.load("assets/Titre RATZ FIGHTER.png")
titre_img = pygame.transform.scale(titre_img, (1300, 500))
pygame.mixer.music.load("assets/intro.mp3")
police_menu = pygame.font.Font("assets/font.ttf", 45)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(5000)
boutton_ok = pygame.mixer.Sound("assets/menuok.wav")
boutton_annu = pygame.mixer.Sound("assets/menuannule.wav")

jeu_en_cours = True  # Variable pour contrôler la boucle principale

# Charger le son du bouton



def Options():
    global jeu_en_cours

    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #Bouton retour
                    if back_button.collidepoint(event.pos):
                        boutton_annu.play()  # Jouer le son du bouton
                        return  # Retourner au menu principal

        fenetre.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

        # Afficher le titre du menu Options
        options_title = police_menu.render("Options", True, (255, 255, 255))
        fenetre.blit(options_title, (250, 100))
        # Bouton de retour
        back_button = pygame.Rect(30, 30, 275, 45)  # largeur = taile police !
        # hitbox = pygame.draw.rect(fenetre,"red",back_button)
        back_text = police_menu.render("Retour", True, (255, 255, 255))
        fenetre.blit(back_text, (30, 30))

        # Ajouter les options :
        # ...

        pygame.display.flip()

#fonction Menu
def Menu():
    global jeu_en_cours

    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_button.collidepoint(event.pos):
                        boutton_ok.play()  # Jouer le son du bouton
                        print("Play appuyé")
                    elif options_button.collidepoint(event.pos):
                        boutton_ok.play()  # Jouer le son du bouton
                        print("Options appuyé")
                        Options()# Appeler la fonction Options
                        print("Retour appuyé")
                    elif exit_button.collidepoint(event.pos):
                        jeu_en_cours = False
                        boutton_ok.play()  # Jouer le son du bouton
                        print("Exit appuyé")

        fenetre.fill((0, 0, 0))

        x = (larg_ecran - titre_img.get_width()) // 2 + 20  # pas bien centré (on rajoute des pixels)
        y = (long_ecran - titre_img.get_height()) // 2 - 80
        fenetre.blit(titre_img, (x, y))

        # Bouton Play
        play_button = pygame.Rect(320, 250, 180, 50) #utiliser la variable hitbox si c'est pas bon
        play_text = police_menu.render("Play", True, (255, 255, 255))
        fenetre.blit(play_text, (325, 255))  # faut bien centrer

        # Bouton Options
        options_button = pygame.Rect(250, 350, 310, 50)
        options_text = police_menu.render("Options", True, (255, 255, 255))
        fenetre.blit(options_text, (250, 355))

        # Bouton Exit
        exit_button = pygame.Rect(250, 450, 310, 50)
        exit_text = police_menu.render("Quitter", True, (255, 255, 255))
        fenetre.blit(exit_text, (250, 455))

        pygame.display.flip()

Menu()
pygame.quit()
sys.exit()
