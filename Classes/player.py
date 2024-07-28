"""
The class representing all info and actions done directly by the player
"""

class Player:
    def __init__(self, name, coins, storageCap, inventory, x, y):
        self.name = name
        self.coins = coins
        self.storageCap = storageCap
        self.inventory = inventory
        self.x = x
        self.y = y

    # Basic info about the player
    def playerInfo(self):
        print("Player Name: " + self.name)
        print("Coins: " + str(self.coins))
        print("Storage Capacity: " + str(self.storageCap) + " lbs" + "\n")
