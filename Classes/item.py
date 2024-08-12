"""
The Class representing each item in the game
"""

class Item:
    def __init__(self, name, value, itemType, itemOrigin, ID):
        self.name = name
        self.value = value
        self.itemType = itemType
        self.itemOrigin = itemOrigin
        self.ID = ID

    # Basic info about the item
    def itemInfo(self):
        print("Item Name: " + self.name)
        print("Item Value: " + str(self.value) + " coins per pound")
        print("Item Type: " + self.itemType)
        print("Item Origin: " + self.itemOrigin + "\n")