"""
The main file the game runs from
"""

from Classes.player import Player
from Classes.island import Island
from Classes.item import Item

# Opening call to action
print("Welcome to high sea merchants! A game of risk and reward, of supply and demand.\nDo you have what it takes"
      " to make a fortune out on the high seas? Do you have\nwhat it takes to become the best merchant in the world? Find out now!\n")

# Testing Stuff Below

# Setup
player = Player('Evan', 300, 100.00, None, 53, 44)
island = Island('Beehive', 100000, 500000.00, None, 53, 44)
item = Item('Lumber', 50, 'raw material', 'agricultural good', 0)

# Printout
"""player.playerInfo()
island.islandInfo()"""
item.itemInfo()
