import pickle
import os

def checkIfPlayerInventoryExistsAndCreateItIfItDoesNot():
    if os.path.exists(inventoryFileName):
        return True
    inventory = {"item1": "sword", "item2": "item"}
    #print(inventory.keys()) use this to get possible functions to use with the dictionary
    with open(inventoryFileName, "wb") as file:
        pickle.dump(inventory, file)
    return False


def getPlayerInventory():
    with open(inventoryFileName, "rb") as file:
        inventory = pickle.load(file)
    print("Loading player inventory data")


def savePlayerInventory():
    pass


def openInventory():
    with open(inventoryFileName, "rb") as file:
        inventory = pickle.load(file)
    print(inventory.keys())
    for key in inventory.keys():
        print(key)
        print(inventory[key])
    print("Loading player inventory data")
    print('inventory contents:', inventory)  # prints the saved data


if __name__ == '__main__':
    exit(0)
else:
    inventoryFileName = "playerInventory.bin"
