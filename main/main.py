import terrainGeneration.generalTerrain as terrain
import inventory.inventoryManager as inventory
import display.screenManager as screen
import inputController.inputManager as playerInput
import combat.combatManager as combat
import time

if __name__ == '__main__':
    print("Finished imports")
    print("starting infinite world of AIDSrpg!")

    fpsLimit = 30
    screenDimensions = 32  # cells rendered in X and Y directions
    playerx = 0
    playery = 0
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "a", "E"]  # If terrain character is in this array the player cannot move onto it.

    while True:
        currentTime = time.time()
        gameMap = terrain.generateCells(playery, playerx, screenDimensions)
        gameMap = combat.renderEnemy(gameMap, screenDimensions)
        gameMap[pindex] = "A"
        image = screen.createBlank(512, 512)
        image = screen.renderScreen(image, gameMap, screenDimensions)
        screen.displayScreen(image)
        playerx, playery = playerInput.inputController(gameMap, screenDimensions, pcollide, pindex, playerx, playery)
        if time.time() - currentTime < 1 / fpsLimit:
            time.sleep(currentTime - time.time() + (1 / fpsLimit))
else:
    exit("You cannot use main as an import as it is not a library")
