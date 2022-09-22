import inventory.inventoryManager as inventory
import combat.lootDrops as loot

# Checks if a trade can be made
def checkTradeAvailable(gameMap, pindex, screenDimensions):
    if gameMap[pindex + 1] in ptrade[0:len(ptrade)] or \
            gameMap[pindex - 1] in ptrade[0:len(ptrade)] or \
            gameMap[pindex - screenDimensions] in ptrade[0:len(ptrade)] or \
            gameMap[pindex + screenDimensions] in ptrade[0:len(ptrade)]:
        return True
    return False


def sellItem():
    # print(inventory.PlayerInventory.inventory.index(loot.itemDropList[0])) # prints the index number of item 0
    if loot.itemDropList[0] in inventory.PlayerInventory.inventory:
        selling = inventory.PlayerInventory.inventory.index(loot.itemDropList[0])
        inventory.PlayerInventory.inventory.pop(selling)
        inventory.PlayerInventory.inventory[0] += 5
        print("sold, +5 gold")
    pass


if __name__ == '__main__':
    exit(0)
else:
    ptrade = ['a']
