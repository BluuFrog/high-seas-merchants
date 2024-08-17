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

    # takes in what items are being given away or taken and coins gained/lost and performs necessary checks and operations on the inventory
    def trade(self, itemGain, gainAmount, itemLost, lossAmount, coinAmount):
        self.coins += coinAmount # if gaining coins coinAmount is positive, if losing its negative

        if itemGain is not None:
            self.inventory.itemList[itemGain.ID].amount += gainAmount

        if itemLost is not None:
            self.inventory.itemList[itemLost.ID].amount -= lossAmount