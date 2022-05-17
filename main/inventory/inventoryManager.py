import pickle
import os


def checkIfPlayerInventoryExistsAndCreateItIfItDoesNot():
    if os.path.exists(inventoryFileName):
        with open(inventoryFileName, "rb") as file:
            return pickle.load(file)
    inventory = [{"item1": "sword"}, {"gold": 999}]
    #   print(inventory.keys()) use this to get possible functions to use with the dictionary
    with open(inventoryFileName, "wb") as file:
        pickle.dump(inventory, file)
    return inventory


def getItem():
    with open(inventoryFileName, "rb") as file:
        inventory = pickle.load(file)
    print("read inventory")
    print(inventory)
    print('gold acquired')
    inventory.append({"gold": 999})  # will add gold later on
    inventory.append({"item2": "armor"})  # will add other items later on
    print(inventory)
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
