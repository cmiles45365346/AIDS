import inventoryManager.inventoryManager as inventory
import terrainGeneration.generalTerrain as terrain
import displayController.screenManager as screen
import combat.combatManager as combat
import trade.tradeManager as trade
import time

if __name__ == '__main__':
    print("starting infinite world of AIDSrpg!")

    screenDimensions = 32  # cells rendered in X and Y directions
    playerx = 0
    playery = 0
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "🏠"]  # If terrain character is in this array the player cannot move onto it.

    while True:
        gameMap = terrain.generateCells(playery, playerx, screenDimensions)
        image = screen.createBlank(512, 512)
        image = screen.renderScreen(image, gameMap, screenDimensions)
        while True:
            screen.displayScreen(image)
        gameMap[pindex] = "A"
        for y in range(screenDimensions):
            print(str(gameMap[0 + (y * screenDimensions):screenDimensions + (y * screenDimensions)]).replace("\'", "", 99999).replace(",", "", 99999).replace("[","|").replace("]", "|"))  # Displays map to console
        pinput = input() + "m"
        pinput = pinput[0].lower()
        if pinput == "q":
            exit("game shut down")
        # General controls for movement in game
        if pinput == "d" and not gameMap[pindex + 1] in pcollide[0:len(pcollide)]:
            playerx += 1
        if pinput == "a" and not gameMap[pindex - 1] in pcollide[0:len(pcollide)]:
            playerx -= 1
        if pinput == "w" and not gameMap[pindex - screenDimensions] in pcollide[0:len(pcollide)]:
            playery -= 1
        if pinput == "s" and not gameMap[pindex + screenDimensions] in pcollide[0:len(pcollide)]:
            playery += 1
        if pinput == "t":
            if trade.checkTradeAvailable(gameMap, pindex, screenDimensions):
                print("Trade can be done")
            else:
                print("Trade cannot be done")
            if combat.checkEnemyNearby(gameMap, pindex):
                print("Enemy nearby")
            else:
                print("no enemy nearby")
        if pinput == "e":  # Opens the inventory so the player can use it.
            pass
else:
    exit("You cannot use main as an import as it is not a library")
