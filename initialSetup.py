"""
The class that creates the global island and item list
"""
from Classes.item import Item
from Classes.island import Island

class InitialSetup:
    def __init__(self, gameType):
        self.gameType = gameType

    # Generates the initial list of items in the game, returns them all in a list
    def generateItemList(self):
        globalItemList = []
        if self.gameType == 'standard':
           globalItemList.append(Item('Lumber', 50, 0, 'raw material', 'agricultural good', 0))
           globalItemList.append(Item('Stone', 80, 0, 'raw material', 'natural resource', 1))
           globalItemList.append(Item('Clay', 60, 0, 'raw material', 'natural resource', 2))
           globalItemList.append(Item('Iron', 120, 0, 'raw material', 'natural resource', 3))
           globalItemList.append(Item('Mortar', 70, 0, 'raw material', 'manufactured good', 4))
           globalItemList.append(Item('Banana', 5, 0, 'foodstuff', 'agricultural good', 5))
           globalItemList.append(Item('Orange', 5, 0, 'foodstuff', 'agricultural good', 6))
           globalItemList.append(Item('Hardtack', 5, 0, 'foodstuff', 'manufactured good', 7))
           globalItemList.append(Item('Jerky', 5, 0, 'foodstuff', 'manufactured good', 8))
           globalItemList.append(Item('Salted Fish', 5, 0, 'foodstuff', 'natural resource', 9))
           globalItemList.append(Item('Sabre', 30, 0, 'equipment', 'manufactured good', 10))
           globalItemList.append(Item('Flintlock Pistol', 60, 0, 'equipment', 'manufactured good', 11))
           globalItemList.append(Item('Rope', 15, 0, 'equipment', 'manufactured good', 12))
           globalItemList.append(Item('Lantern Oil', 20, 0, 'equipment', 'agricultural good', 13))
           globalItemList.append(Item('Whetstone', 15, 0, 'equipment', 'natural resource', 14))
           globalItemList.append(Item('Rum', 80, 0, 'luxury', 'agricultural good', 15))
           globalItemList.append(Item('Sugar', 40, 0, 'luxury', 'agricultural good', 16))
           globalItemList.append(Item('Gold', 200, 0, 'luxury', 'natural resource', 17))
           globalItemList.append(Item('Pearl', 160, 0, 'luxury', 'natural resource', 18))
           globalItemList.append(Item('Silk Garments', 140, 0, 'luxury', 'manufactured good', 19))
        return globalItemList

    # Generates the initial list of islands in the game, returns them all in a list
    def generateIslandList(self):
        globalIslandList = []
        if self.gameType == 'standard':
            globalIslandList.append(Island('Beehive', 1000000, 500000.00, None, 7, 13))
            globalIslandList.append(Island('Varyeho', 150000, 700000.00, None, 13, 39))
            globalIslandList.append(Island('Crawford', 120000, 9000000.00, None, 53, 27))
            globalIslandList.append(Island('Kashwana', 200000, 1000000.00, None, 64, 74))
        return globalIslandList