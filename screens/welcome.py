import pygame
from components import Button, Textbox
from .base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        """Creates three buttons on the screen along with the game title"""
        super().__init__(window)
        pygame.font.init()
        self.start = Button(self.window, pos=(125,400),text='Start')
        self.exit = Button(self.window, pos=(400,400),text='Exit')
        self.help = Button(self.window, pos=(675,400),text='Help')
        self.title1 = Textbox(self.window, pos_y = 100, text="Genshin Slime", font_size=80)
        self.title2 = Textbox(self.window, pos_y = 200, text="Shooter", font_size=80)


    def draw(self):
        """Draws the buttons and game title"""
        self.window.fill((255, 255, 255))
        background = pygame.image.load("assets/bg_black.png")
        self.window.blit(background, (0,0))
        self.start.draw()
        self.exit.draw()
        self.help.draw()
        self.title1.draw()
        self.title2.draw()

    def manage_event(self, event):
        if event.type == pygame.QUIT: 
            self.running = False
            self.next_screen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:                  
                if self.start.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = "select"

                if self.exit.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = False

                if self.help.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = "help"