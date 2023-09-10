import pygame

class Button:
    """Buttons on the screen, generally to move screens"""
    def __init__(self, screen, pos: tuple,  text:str, font_size=36, text_y=None, size=(200,100)):
        self.screen = screen
        self.button = pygame.Surface(size)
        # fill button with black
        self.button.fill((0, 0, 0))
        font = pygame.font.Font("assets/zhcn.ttf", font_size)
        img = font.render(text, True, (255, 255, 255))
        text_size = font.size(text)
        # if y coordinate of text not specified, blit text vertically centered
        if text_y == None:
            text_y = (size[1] - text_size[1]) / 2
        # always blit text horizontally centered
        text_x = (size[0] - text_size[0]) / 2
        self.button.blit(img, (text_x, text_y))
        self.rect = self.button.get_rect()
        self.rect.topleft = pos
        # make button slightly transparent for aesthetics
        self.button.set_alpha(200)

    def draw(self):
        self.screen.blit(self.button, self.rect)