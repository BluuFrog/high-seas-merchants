"""
The main file the game runs from
"""

# imports
import pygame
from Classes.player import Player
from Classes.inventory import Inventory
from Classes.playerBoat import PlayerBoat
from Python_Projects.Learning.Learning_Projects.Large_Projects.HighSeasMerchants.initialSetup import InitialSetup


# Backend Setup
setupObject = InitialSetup('standard')
globalItemList = setupObject.generateItemList()
globalIslandList = setupObject.generateIslandList()
setupObject.openingText()

player = Player('Joshua', 300, 100.00, Inventory(True, globalItemList), 7, 13)

# Pygame Setup
pygame.init() # Initial setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
inTitle = True

pygame.display.set_caption("High Seas Merchants") # Window name and icon
icon = pygame.image.load('Assets/IconHSM.png')
pygame.display.set_icon(icon)

titleScreen = pygame.image.load('Assets/TitleScreenHSM.png') # Title screen
screen.fill(color=(153, 204, 255))
font = pygame.font.SysFont("constantia", 34, False, False)
text = font.render("Press any key to continue", True, pygame.Color((115, 62, 57)))
pygame.Surface.blit(screen, titleScreen, (500, 125))
pygame.Surface.blit(screen, text, (570, 600))

pBoat = PlayerBoat()
pGroup = pygame.sprite.Group()
pGroup.add(pBoat)


while running: # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if inTitle: # Code to make title screen disappear when a key is pressed
            if event.type == pygame.KEYDOWN:
                screen.fill(color=(153, 204, 255))
                inTitle = False
                pygame.sprite.Group.draw(pGroup, screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            pBoat.rect.y += 10
            #pGroup.clear(screen, screen)
            pygame.sprite.Group.draw(pGroup, screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Testing Below
#player.inventory.addItem(globalItemList[2], 5)
#player.inventory.addItem(globalItemList[8], 7)
#player.inventory.addItem(globalItemList[17], 3)
#player.inventory.removeItem(globalItemList[8], 5)
#player.trade(globalItemList[4], 7, globalItemList[2], 4, 200)
#player.inventory.showItems()

