import json
import os


def getPlayerInventory():
    file = open("playerInventory.json", "r")
    print("Loading player inventory data")
    data = json.load(file)

    print("Decoded data from json file")
    file.close()


def savePlayerInventory():
    pass


if __name__ == '__main__':
    exit(0)
