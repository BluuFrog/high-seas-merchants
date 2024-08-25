"""
The class representing the player's boat that is movable by the player
"""
import pygame.sprite

class PlayerBoat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Call sprite class constructor

        self.image = pygame.image.load('Assets/IconHSM.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
