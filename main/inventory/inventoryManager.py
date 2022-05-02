import json
import os

def checkIfPlayerInventoryExistsAndCreateItIfItDoesNot():
    if os.path.exists(inventoryFileName):
        return True
    file = open(inventoryFileName, "w")  # Creates file that didn't exist with basic template
    file.close()
    return False


def getPlayerInventory():
    file = open(inventoryFileName, "r")
    print("Loading player inventory data")
    data = json.load(file)

    print("Decoded data from json file")
    file.close()


def savePlayerInventory():
    pass


if __name__ == '__main__':
    inventoryFileName = "playerInventory.json"
    exit(0)
