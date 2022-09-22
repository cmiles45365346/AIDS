import inventory.inventoryManager as inventory
import secrets
import time

def itemAquire():
    inventory.PlayerInventory.inventory[0] += 10  # you get 10 pennies for combat, subject to change, prob should be random but seed go brr
    inventory.PlayerInventory.inventory.append(randomItem(itemDropList))


def randomItem(loot):
    item = secrets.choice(loot)
    print("{} acquired.".format(item))
    return item


itemDropList = ["biffed boots", "dinky dagger", "shitty shirt", "grimey greaves", "hobo helmet"]
