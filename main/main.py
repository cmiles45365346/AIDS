import terrainGeneration.generalTerrain as terrain
import inventory.inventoryManager as inventory
import display.screenManager as screen
import inputController.inputManager as playerInput
import time

if __name__ == '__main__':
    print("Finished imports")
    print("starting infinite world of AIDSrpg!")

    screenDimensions = 32  # cells rendered in X and Y directions
    playerx = 0
    playery = 0
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "🏠"]  # If terrain character is in this array the player cannot move onto it.

    while True:
        gameMap = terrain.generateCells(playery, playerx, screenDimensions)
        gameMap[pindex] = "A"
        image = screen.createBlank(512, 512)
        image = screen.renderScreen(image, gameMap, screenDimensions)
        screen.displayScreen(image)
        playerx, playery = playerInput.inputController(gameMap, screenDimensions, pcollide, pindex, playerx, playery)
else:
    exit("You cannot use main as an import as it is not a library")
