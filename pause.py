def pause():
    # font
    CRT_GREEN = (20, 255, 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    small_font = pygame.font.SysFont('courier', 15)
    big_font = pygame.font.SysFont('courier', 20)
    outline_color = (0, 0, 255)
    resume = pygame.Rect(35, 125, 125, 35)

    class Button:
        def __init__(self, text, x, y, width, height):
            self.text = text
            self.rect = pygame.Rect(x, y, width, height)
            self.font = pygame.font.SysFont('courier', 15)

        def draw(self, screen):

            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, black, self.rect)
            else:
                pygame.draw.rect(screen, black, self.rect)
            text_surface = self.font.render(self.text, True, CRT_GREEN)
            screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

        def is_clicked(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
            return False

    # window dimensions
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))

    #assest
    background = pygame.image.load('test_background_imresizer.jpg')
    w_text = pygame.image.load('W.png')


    # Buttons
    resume_button = Button("Resume Game", 14, 105, 75, 35)
    music_vup = Button("+", 160,185, 30,30)
    music_vdown = Button("-", 135,185, 30,30)
    SFX_vup = Button("+", 160,145, 30,30)
    SFX_vdown = Button("-", 135,145, 30,30)
    fullscreen_button = Button("Fullscreen", 14, 225, 100, 35)
    exit_button = Button("Exit Game", 150, 300, 125, 35)
    # main loop
    running = True
    while running:
         screen.fill((0,0,0))
         #mouse position
         mouse_pos = pygame.mouse.get_pos()

         #Drawing button
         resume_button.draw(screen)
         fullscreen_button.draw(screen)
         exit_button.draw(screen)
         music_vup.draw(screen)
         music_vdown.draw(screen)
         SFX_vup.draw(screen)
         SFX_vdown.draw(screen)

         # Outline
         pygame.draw.rect(screen, outline_color, resume_button.rect, 3)
         #pygame.draw.rect(screen, outline_color, fullscreen_button.rect, 3)
         # outline color change
         if resume_button.rect.collidepoint(mouse_pos):
             pygame.draw.rect(screen, CRT_GREEN, resume_button.rect, 3)
         resume_button.draw(screen)
         #if fullscreen_button.rect.collidepoint(mouse_pos):
             #pygame.draw.rect(screen, CRT_GREEN, fullscreen_button.rect, 3)
             #fullscreen_button.draw(screen)


         #Render text
         w = small_font.render("Move UP [W]", True, CRT_GREEN)
         a = small_font.render("Move RIGHT [A]", True, CRT_GREEN)
         s = small_font.render("Move LEFT [S]", True, CRT_GREEN)
         d = small_font.render("Move DOWN [D]", True, CRT_GREEN)
         bullet = small_font.render("Shoot [Left Click]", True, CRT_GREEN)
         pause_unpause= small_font.render("Pause Game [ESC]", True, CRT_GREEN)
         music = small_font.render("Music Volume", True, CRT_GREEN)
         SFX = small_font.render("SFX Volume", True, CRT_GREEN)
         game_pause = big_font.render("Game Pause", True, CRT_GREEN)
            #screen.blit(w_text, (0, 0))
            #screen.blit(background,(0,0))
        #Display text
         screen.blit(game_pause, (145, 45))
         screen.blit(w, (280, 115))
         screen.blit(a, (253, 137))
         screen.blit(s, (262, 160))
         screen.blit(d, (262, 185))
         screen.blit(bullet, (216, 210))
         screen.blit(pause_unpause, (233, 235))
         screen.blit(music, (25, 195))
         screen.blit(SFX, (25, 155))


         pygame.display.flip()

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Clicking the button
            if resume_button.is_clicked(event):
                print("Resume")
            if fullscreen_button.is_clicked(event):
                print("Fullscreen")
            if exit_button.is_clicked(event):
                print("Exit Game")
            if music_vup.is_clicked(event):
                print("Music vup")
            if music_vdown.is_clicked(event):
                print("Music vdown")
            if SFX_vup.is_clicked(event):
                print("SFX vup")
            if SFX_vdown.is_clicked(event):
                print("SFX vdown")

    return

pause()
