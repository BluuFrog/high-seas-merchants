"""
The class representing each island in the game
"""

class Island:
    def __init__(self, name, coins, storageCap, inventory, x, y):
        self.name = name
        self.coins = coins
        self.storageCap = storageCap
        self.inventory = inventory
        self.x = x
        self.y = y

    # Basic info about island that the player needs
    def islandInfo(self):
        print("Island Name: " + self.name)
        print("Island Location: X: " + str(self.x) + " Y: " + str(self.y) + "\n")
