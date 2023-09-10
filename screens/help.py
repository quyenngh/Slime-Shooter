import pygame
from components import Button, Textbox
from .base_screen import BaseScreen


class HelpScreen(BaseScreen):
    def __init__(self, window):
        """Displays game instructions and a button to go back to welcome screen"""
        super().__init__(window)
        pygame.font.init()
        self.back = Button(self.window, pos=(400,400),text='Back')
        instructions = ["Use the arrow keys to move around", 
                        "Press space to fire an attack", 
                        "Each slime is worth 10 points",
                        "Touch coins to collect them",
                        "Each coin is worth 5 points",
                        "Game will be over when a slime touches the character"]
        self.instructions = [Textbox(self.window, pos_y = (i*50)+75, text=instructions[i], font_size=30) for i in range(len(instructions))]

    def draw(self):
        """Draws the screen"""
        self.window.fill((255, 255, 255))
        background = pygame.image.load("assets/bg_black.png")
        self.window.blit(background, (0,0))
        self.back.draw()
        for instruction in self.instructions:
            instruction.draw()

    def manage_event(self, event):
        if event.type == pygame.QUIT: 
            self.running = False
            self.next_screen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:                  
                if self.back.rect.collidepoint(pygame.mouse.get_pos()):
                    self.running = False
                    self.next_screen = "welcome"
