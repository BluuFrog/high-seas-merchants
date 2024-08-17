"""
The main file the game runs from
"""

# imports
from Classes.player import Player
from Classes.inventory import Inventory
from Python_Projects.Learning.Learning_Projects.Large_Projects.HighSeasMerchants.initialSetup import InitialSetup

# Opening text
print("Welcome to high sea merchants! A game of risk and reward, of supply and demand.\nDo you have what it takes"
      " to make a fortune out on the high seas? Do you have\nwhat it takes to become the best merchant in the world? Find out now!\n")


# Setup
setupObject = InitialSetup('standard')
globalItemList = setupObject.generateItemList()
globalIslandList = setupObject.generateIslandList()

player = Player('Joshua', 300, 100.00, Inventory(True, globalItemList), 53, 44)

# Testing Below
player.inventory.addItem(globalItemList[2], 5)
player.inventory.addItem(globalItemList[8], 7)
player.inventory.addItem(globalItemList[17], 3)
player.inventory.removeItem(globalItemList[8], 5)
player.inventory.showItems()
