import pygame
import random
import math

class Enemy:
    """Enemy that floats down the screen"""
    def __init__(self, icon):
        self.icon = pygame.image.load(icon)
        # enemy position is randomly generated on the right half of the screen
        self.x = random.randint(800,1000)
        self.y = random.randint(0,520)
        # enemy speed is also slightly random
        self.speed = random.randint(-20,-10) / 2

    def display(self, screen, x, y):
        screen.blit(self.icon, (x, y))
    
    def reset(self):
        """Resets enemy to a randomly generated position"""
        self.x = random.randint(850,1000)
        self.y = random.randint(0,520)

    def fly(self):
        """Floats enemy across the screen according to speed, reset its position if out of bounds"""
        self.x += self.speed
        if self.x <= -10:
            self.reset()
    
    def collision(self, target):
        """Detect collision with distance formula, if close enough return True"""
        distance = math.sqrt((self.x-target.x)**2 + (self.y-target.y)**2)
        if distance < 100:
            return True
        else: 
            return False