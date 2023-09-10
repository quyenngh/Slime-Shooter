import pygame
from components import Player, Enemy, Attack, Textbox
from .base_screen import BaseScreen

class GameScreen(BaseScreen):
    def __init__(self, window):
        """The game screen has a player that kills enemies"""
        super().__init__(window)
        # sprites
        self.player = Player("assets/childe.png")
        no_of_enemies = 5
        self.enemies = [Enemy("assets/slime80.png") for i in range(no_of_enemies)]
        # although coins are not enemies, they need the same attributes and methods
        self.coins = [Enemy("assets/mora100.png") for i in range(no_of_enemies)]
        no_of_attacks = 2
        self.attacks = [Attack("assets/atk90.png") for i in range(no_of_attacks)]

    def draw(self):
        """Draw the screen"""
        characters = ["aether", "xiao", "childe", "xingqiu", "kokomi", "sara"]
        # use character icon based on selection from select screen
        for i in range(len(characters)):
            if self.persistent.get("selection", 0) == i:
                self.player.icon = pygame.image.load("assets/{}.png".format(characters[i]))
        
        # blit background
        self.window.fill((255, 255, 255))
        background = pygame.image.load("assets/bg_black.png")
        self.window.blit(background, (0,0))

        # show score
        self.score = Textbox(self.window, pos_y=10, text="Score : " + str(self.player.score), pos_x=10)
        self.score.draw()

        # player movement
        self.player.horizontal_move()
        self.player.vertical_move()
        self.player.display(self.window, self.player.x, self.player.y)

        # attacking enemies and detect collision
        for attack in self.attacks:
            if attack.state == "fire":
                attack.fire(self.window, attack.x, attack.y)
                attack.fly()

        # collecting coins
        for coin in self.coins:
            player_collision = coin.collision(self.player)
            if player_collision:
                self.player.score += 5
                coin.reset()
            coin.display(self.window, coin.x, coin.y)
            coin.fly()

        # displaying enemies
        for enemy in self.enemies:
            # detect enemy collision with player for game over
            player_collision = enemy.collision(self.player)
            if player_collision:
                # assign score and reload everything before moving to game over screen
                self.persistent["score"] = self.player.score
                self.player.reset()
                for attack in self.attacks:
                    attack.load()
                for enemy in self.enemies:
                    enemy.reset()
                self.running = False
                self.next_screen = "game_over"

            # detect attack collision for score
            for attack in self.attacks:
                atk_collision = enemy.collision(attack)
                if atk_collision:
                    self.player.score += 10
                    enemy.reset()
                    attack.load()
            enemy.display(self.window, enemy.x, enemy.y)
            enemy.fly()

    def manage_event(self, event):
        if event.type == pygame.QUIT: 
            self.running = False
            self.next_screen = False

        if event.type == pygame.KEYDOWN:
            # player start moving
            if event.key == pygame.K_RIGHT:
                self.player.move_x = 5
            if event.key == pygame.K_LEFT:
                self.player.move_x = -5
            if event.key == pygame.K_UP:
                self.player.move_y = -5
            if event.key == pygame.K_DOWN:
                self.player.move_y = 5

            # player attack
            if event.key == pygame.K_SPACE:
                for attack in self.attacks:
                    if attack.state == "ready":
                        attack.y = self.player.y
                        attack.x = self.player.x
                        attack.fire(self.window, attack.x, attack.y)

        # player stop moving
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                self.player.move_x = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                self.player.move_y = 0