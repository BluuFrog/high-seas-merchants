"""
The main file the game runs from
"""

from Classes.player import Player
from Classes.island import Island

# Opening call to action
print("Welcome to high sea merchants! A game of risk and reward, of supply and demand.\nDo you have what it takes"
      " to make a fortune out on the high seas? Do you have\nwhat it takes to become the best merchant in the world? Find out now!\n")

# Testing Stuff Below
player = Player('Test', 500, 100.00, None, 53, 44)
island = Island('Beehive', 100000, 500000.00, None, 53, 44)

player.playerInfo()
island.islandInfo()
