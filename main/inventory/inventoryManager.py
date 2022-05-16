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

    print(data)
    file.close()


def savePlayerInventory():
    pass


def openInventory():
    with open(inventoryFileName) as f:  # opens the file again, works probably cause not >,'w'
        items = json.load(f)  # saves the file into a variable
    print('inventory contents:', items)  # prints the saved data


if __name__ == '__main__':
    exit(0)
else:
    inventoryFileName = "playerInventory.json"
