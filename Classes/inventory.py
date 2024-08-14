"""
The Class representing an entities inventory
"""

class Inventory:

    itemList = [] # Where items will be held
    for index in range(0, 21):
        itemList.append(-1) # Filling list with placeholder 1's, maybe populate it with the global item list but everything set to 0 amount

    def __init__(self, isPlayer):
        self.isPlayer = isPlayer

    # Adds item to list if not there yet, just adds more to amount if already there
    def addItem(self, item, amount):
        if self.itemList[item.ID] == -1:
            self.itemList[item.ID] = item
            self.itemList[item.ID].amount = amount
        else:
            self.itemList[item.ID].amount += amount

    # Shows all items in list that is greater than 0, will be changed that way on thursday likely
    def showItems(self):
        for index in range(0, 21):
            if self.itemList[index] != -1:
                print(self.itemList[index].name + ": " + str(self.itemList[index].amount))
        print("") # to make a new line after all the inventory has been shown