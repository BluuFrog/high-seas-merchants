"""
The Class representing an entities inventory
"""

class Inventory:

    def __init__(self, isPlayer, itemList):
        self.isPlayer = isPlayer
        self.itemList = itemList

    # Adds item to list if not there yet, just adds more to amount if already there
    def addItem(self, item, amount):
        if self.itemList[item.ID] == -1:
            self.itemList[item.ID] = item
            self.itemList[item.ID].amount = amount
        else:
            self.itemList[item.ID].amount += amount

    # Shows all items in list that is greater than 0, will be changed that way on thursday likely
    def showItems(self):
        for index in range(0, 20):
            if self.itemList[index].amount > 0:
                print(self.itemList[index].name + ": " + str(self.itemList[index].amount))
        print("") # to make a new line after all the inventory has been shown