import pygame

class Textbox:
    """To display text without using buttons"""
    def __init__(self, screen, pos_y,  text:str, font_size=20, pos_x=None):
        self.screen = screen
        self.pos_y = pos_y
        font = pygame.font.Font("assets/zhcn.ttf", font_size)
        self.img = font.render(text, True, (255, 255, 255))
        text_size = font.size(text)
        # if x coordinate not specified, blit text horizontally centered 
        if pos_x == None:
            self.pos_x = (1000 - text_size[0]) / 2
        else:
            self.pos_x = pos_x

    def draw(self):
        self.screen.blit(self.img, (self.pos_x, self.pos_y))