"""
The Class representing an entities inventory
"""

class Inventory:
    def __init__(self, isPlayer, itemList):
        self.isPlayer = isPlayer
        self.itemList = itemList

    # Adds to the amount attribute of an item
    def addItem(self, item, amount):
        self.itemList[item.ID].amount += amount

    # Subtracts from the amount attribute of an item
    def removeItem(self, item, amount):
        self.itemList[item.ID].amount -= amount

    # Shows all items in list that have amounts greater than 0
    def showItems(self):
        for index in range(0, 20):
            if self.itemList[index].amount > 0:
                print(self.itemList[index].name + ": " + str(self.itemList[index].amount))
        print("") # to make a new line after all the inventory has been shown