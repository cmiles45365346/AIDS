import pickle
import os


def checkIfPlayerInventoryExistsAndCreateItIfItDoesNot():
    if os.path.exists(inventoryFileName):
        return True
    inventory = [{"item1": "sword"}]
    inventory.append({"gold": 999})
    #   print(inventory.keys()) use this to get possible functions to use with the dictionary
    with open(inventoryFileName, "wb") as file:
        pickle.dump(inventory, file)
    return False


def getItem():
    print('gold acquired')
    inventory.append({"gold": 999})  # will add gold later on
    inventory.append({"item2": "armor"})  # will add other items later on
    savePlayerInventory(inventory)


def savePlayerInventory(inventory):
    with open(inventoryFileName, "wb") as file:
        pickle.dump(inventory, file)


def openInventory():
    with open(inventoryFileName, "rb") as file:
        inventory = pickle.load(file)
    for index in inventory:
        print(index)
        for key in index.keys():
            print(index[key])


if __name__ == '__main__':
    exit(0)
else:
    inventoryFileName = "playerInventory.bin"
