import pygame

from components import Button, Textbox

from .base_screen import BaseScreen


class GameOverScreen(BaseScreen):
    def __init__(self, window):
        """The game over screen has buttons to retry with the same character, go back to welcome screen, or exit the game"""
        super().__init__(window)
        self.retry = Button(self.window, pos=(125,400), text='Retry')
        self.exit = Button(self.window, pos=(400,400), text='Exit')
        self.home = Button(self.window, pos=(675,400), text='Home')
        self.over = Textbox(self.window, pos_y = 100, text="GAME OVER", font_size=80)

    def draw(self):
        """Draw the sprites"""
        self.window.fill((255, 255, 255))
        background = pygame.image.load("assets/bg_black.png")
        self.window.blit(background, (0,0))
        self.retry.draw()
        self.exit.draw()
        self.home.draw()
        self.over.draw()
        score = Textbox(self.window, pos_y = 200, text="Score : " + str(self.persistent["score"]), font_size=36)
        score.draw()

    def manage_event(self, event):
        if event.type == pygame.QUIT: 
            self.running = False
            self.next_screen = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # if exit there is no next screen
                if self.exit.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = False

                # if home then go back to welcome screen
                if self.home.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = "welcome"

                # if retry then go to screen and play again with same character
                if self.retry.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = "game"