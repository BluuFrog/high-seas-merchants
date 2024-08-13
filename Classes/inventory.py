"""
The Class representing an entities inventory
"""

class Inventory:

    itemList = []

    def __init__(self, isPlayer):
        self.isPlayer = isPlayer

    def addItem(self, item):
        self.itemList.insert(item.ID, item)

    def showItems(self, index):
        for item in self.itemList:
            print(item.name)