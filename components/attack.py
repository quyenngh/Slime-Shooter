import pygame

class Attack:
    """The attack that fires when the player presses space"""
    def __init__(self, icon):
        self.icon = pygame.image.load(icon)        
        self.x = -10
        self.y = -10
        self.speed = 25
        self.state = "ready" # when press space: ready -> fire

    def fire(self, screen, x, y):
        """Changes attack state to fire and blits the attack right in front of the character"""
        self.state = "fire"
        screen.blit(self.icon, (x+72, y+10))

    def load(self):
        """Reloads the attack by setting its coordinates back the original position outside the frame,
        then changing state to ready for next fire."""
        self.x = -10
        self.y = -10
        self.state = "ready"
    
    def fly(self):
        """Changes the attack's x coordinates according to the set speed. 
        If it doesn't collide with an enemy and goes out of bounds, reload it."""
        self.x += self.speed
        if self.x >= 1000:
            self.load()