import pygame

class Player:
    """Character controlled by player throughout the game"""
    def __init__(self, icon):
        self.score = 0
        self.icon = pygame.image.load(icon)
        self.x = 100
        self.y = 270
        self.move_x = 0.0
        self.move_y = 0.0

    def display(self, screen, x, y):
        screen.blit(self.icon, (x, y))

    def horizontal_move(self):
        """Move horizontally across screen according to set speed. If at borders of display stay in place."""
        self.x += self.move_x
        if self.x <= -13:
            self.x = -13
        if self.x >= 913:
            self.x = 913

    def vertical_move(self):
        """Move vertically across screen according to set speed. If at borders of display stay in place."""
        self.y += self.move_y
        if self.y <= 0:
            self.y = 0
        if self.y >= 500:
            self.y = 500

    def reset(self):
        """Reset character to original position after game ends so they don't immediately die upon retry."""
        self.x = 100
        self.y = 270
        self.move_x = 0.0
        self.move_y = 0.0
        self.score = 0