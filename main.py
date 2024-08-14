"""
The main file the game runs from
"""

# imports
from Classes.player import Player
from Classes.island import Island
from Classes.item import Item
from Classes.inventory import Inventory

# Opening text
print("Welcome to high sea merchants! A game of risk and reward, of supply and demand.\nDo you have what it takes"
      " to make a fortune out on the high seas? Do you have\nwhat it takes to become the best merchant in the world? Find out now!\n")


# Setup - replace with method calls, populating a global item list and island list
playerInventory = Inventory(True)
player = Player('Joshua', 300, 100.00, playerInventory, 53, 44)
island = Island('Beehive', 100000, 500000.00, None, 53, 44)
item = Item('Lumber', 50, 0, 'raw material', 'agricultural good', 0)
item2 = Item('Stone', 80, 0, 'raw material', 'natural resource', 1)

# Testing Below
#player.playerInfo()
#island.islandInfo()
#item.itemInfo()
player.inventory.addItem(item, 5)
player.inventory.addItem(item, 5)
player.inventory.addItem(item2, 3)
player.inventory.showItems()
