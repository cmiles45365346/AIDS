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
    data = {
        'items': [
            'sword'
        ]
    }
    with open(inventoryFileName, 'w') as f:  # opens the inventory file
        json.dump(data, f, indent=2)  # writes to the file
        #  close(inventoryFileName)


def openInventory():
    with open(inventoryFileName) as f:  # opens the file again, works probably cause not >,'w'
        info = json.load(f)  # saves the file into a variable
    print('inventory conents:', info)  # prints the saved data
    pass


if __name__ == '__main__':
    exit(0)
else:
    inventoryFileName = "playerInventory.json"
