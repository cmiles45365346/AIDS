import terrainGeneration.generalTerrain as terrain
import inventory.inventoryManager as inventory
import display.screenManager as screen
import inputController.inputManager as playerInput
import combat.combatManager as combat
import time

if __name__ == '__main__':
    print("Finished imports")
    print("starting infinite world of AIDSrpg!")

    fpsLimit = 20  # Limit of how many frames are rendered per second
    screenDimensions = 32  # cells rendered in X and Y directions
    playerx = 0  # the players x coordinate
    playery = 0  # the players y coordinate
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "a", "E"]  # The player cannot move onto these characters
    inventoryData = inventory.checkIfPlayerInventoryExistsAndCreateItIfItDoesNot()
    inventory.savePlayerInventory(inventoryData)
    for i in range(500):  # Generates 500 random enemies around the player
        combat.genEnemies(playerx, playery)  # Actually random because seed not set yet

    while True:
        currentTime = time.time()

        gameMap = terrain.generateCells(playery, playerx, screenDimensions)
        gameMap = combat.renderEnemy(gameMap, screenDimensions, playerx, playery)
        gameMap[pindex] = "A"  # Players character is A

        image = screen.createBlank(512, 512)
        image = screen.renderScreen(image, gameMap, screenDimensions)
        screen.displayScreen(image)

        playerx, playery = playerInput.inputController(gameMap, screenDimensions, pcollide, pindex, playerx, playery)

        if time.time() - currentTime < 1 / fpsLimit:
            time.sleep(currentTime - time.time() + (1 / fpsLimit))
else:
    exit("You cannot use main as an import as it is not a library")
