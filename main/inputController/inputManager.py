import combat.combatManager as combat
import trade.tradeManager as trade
import inventory.inventoryManager as inventory
import combat.lootDrops as loot
import keyboard


def inputController(gameMap, screenDimensions, pcollide, pindex, playerx, playery):
    if keyboard.is_pressed("esc"):
        exit("game shut down")
    # Controls in game
    if keyboard.is_pressed("s") and not gameMap[pindex + 1] in pcollide[0:len(pcollide)]:
        playerx += 1
    if keyboard.is_pressed("w") and not gameMap[pindex - 1] in pcollide[0:len(pcollide)]:
        playerx -= 1
    if keyboard.is_pressed("a") and not gameMap[pindex - screenDimensions] in pcollide[0:len(pcollide)]:
        playery -= 1
    if keyboard.is_pressed("d") and not gameMap[pindex + screenDimensions] in pcollide[0:len(pcollide)]:
        playery += 1
    if keyboard.is_pressed("t"):
        if trade.checkTradeAvailable(gameMap, pindex, screenDimensions):
            print("Trade can be done")
            trade.sellItem()
        else:
            print("Trade cannot be done")
        if combat.checkEnemyNearby(gameMap, pindex, screenDimensions):
            # print("Enemy nearby")
            loot.itemAquire()
        # else:
            # print("no enemy nearby")

    if keyboard.is_pressed("e"):  # Opens the inventory so the player can use it.
        inventory.PlayerInventory.openInventory()

    return playerx, playery
