"""
The main file the game runs from
"""

# imports
import pygame
from Classes.player import Player
from Classes.inventory import Inventory
from Python_Projects.Learning.Learning_Projects.Large_Projects.HighSeasMerchants.initialSetup import InitialSetup


# Backend Setup
setupObject = InitialSetup('standard')
globalItemList = setupObject.generateItemList()
globalIslandList = setupObject.generateIslandList()
setupObject.openingText()

player = Player('Joshua', 300, 100.00, Inventory(True, globalItemList), 7, 13)

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("High Seas Merchants")
icon = pygame.image.load('Assets/IconHSM.png')
pygame.display.set_icon(icon)

titleScreen = pygame.image.load('Assets/TitleScreenHSM.png')
screen.fill(color=(153, 204, 255))
pygame.Surface.blit(screen, titleScreen, (500, 200))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Testing Below
player.inventory.addItem(globalItemList[2], 5)
player.inventory.addItem(globalItemList[8], 7)
player.inventory.addItem(globalItemList[17], 3)
player.inventory.removeItem(globalItemList[8], 5)
player.trade(globalItemList[4], 7, globalItemList[2], 4, 200)
player.inventory.showItems()
