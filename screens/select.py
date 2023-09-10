import pygame

from components import Button

from .base_screen import BaseScreen


class SelectScreen(BaseScreen):
    def __init__(self, window):
        """Screen where player can select a character image out of 6 button options"""
        super().__init__(window)
        self.aether = Button(self.window, size=(200, 200), pos=(100,75),text='Aether', font_size=20, text_y=28)
        self.xiao = Button(self.window, size=(200, 200), pos=(400,75),text='Xiao', font_size=20, text_y=28)
        self.childe = Button(self.window, size=(200, 200), pos=(700,75),text='Childe', font_size=20, text_y=28)
        self.xingqiu = Button(self.window, size=(200, 200), pos=(100,350),text='Xingqiu', font_size=20, text_y=28)
        self.kokomi = Button(self.window, size=(200, 200), pos=(400,350),text='Kokomi', font_size=20, text_y=28)
        self.sara = Button(self.window, size=(200, 200), pos=(700,350),text='Kujou Sara', font_size=20, text_y=28)
        self.buttons = [self.aether, self.xiao, self.childe, self.xingqiu, self.kokomi, self.sara]
        characters = ["aether", "xiao", "childe", "xingqiu", "kokomi", "sara"]
        self.icons = [pygame.image.load("assets/{}.png".format(characters[i])) for i in range(len(characters))]

    def draw(self):
        """Draw the buttons and characters"""
        self.window.fill((255, 255, 255))
        background = pygame.image.load("assets/bg_black.png")
        self.window.blit(background, (0,0))
        for button in self.buttons:
            button.draw()
        i=0
        for y in range(150, 451, 275):
            for x in range(150,751,300):
                self.window.blit(self.icons[i], (x, y))
                i+=1

    def manage_event(self, event):
        if event.type == pygame.QUIT: 
            self.running = False
            self.next_screen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in self.buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        # for any button, make selection key in persistent index of that button for 
                        # character icon in game screen, then go to game screen
                        self.persistent["selection"] = self.buttons.index(button)
                        self.running = False
                        self.next_screen = "game"