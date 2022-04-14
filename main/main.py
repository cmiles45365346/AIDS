import inventoryManager.inventoryManager as inventory
import terrainGeneration.generalTerrain as terrain
import displayController.screenManager as screen
import combat.combatManager as combat
import trade.tradeManager as trade

if __name__ == '__main__':
    print("starting infinite world of AIDSrpg!")

    screenDimensions = 32  # cells rendered in X and Y directions
    camx = 0
    camy = 0
    pindex = 496
    pcollide = ["∧", "🏠"]  # If terrain character is in this array the player cannot move onto it.

    while True:
        map = terrain.generateCells(camy, camx)
        map[pindex] = "A"
        for y in range(screenDimensions):
            print(str(map[0 + (y * screenDimensions):screenDimensions + (y * screenDimensions)]).replace("\'", "", 99999).replace(",", "", 99999).replace("[","|").replace("]", "|"))  # Displays map to console
        pinput = input() + "m"
        pinput = pinput[0].lower()
        if pinput == "q":
            exit("game shut down")
        # General controls for movement in game
        if pinput == "d" and not map[pindex + 1] in pcollide[0:len(pcollide)]:
            camx += 1
        if pinput == "a" and not map[pindex - 1] in pcollide[0:len(pcollide)]:
            camx -= 1
        if pinput == "w" and not map[pindex - 32] in pcollide[0:len(pcollide)]:
            camy -= 1
        if pinput == "s" and not map[pindex + 32] in pcollide[0:len(pcollide)]:
            camy += 1
        if pinput == "t":
            if trade.checkTradeAvailable(map, pindex):
                print("Trade can be done")
            else:
                print("Trade cannot be done")
        if pinput == "e":  # Opens the inventory so the player can use it.
            pass
else:
    exit("You cannot use main as an import as it is not a library")
