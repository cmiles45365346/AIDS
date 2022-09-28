import inventory.inventoryManager as inventory
import secrets
import time


def item_acquired():
    inventory.PlayerInventory.inventory[0] += 10  # you get 10 pennies for combat, subject to change, prob should be random but seed go brr
    item = random_item(itemDropList)
    if item != None:  # if an item is acquird and is call
        inventory.PlayerInventory.inventory.append(item)


def random_item(loot):
    if secrets.choice(range(0, 3)) == 0:  # 1/3 Chance to get an item
        item = secrets.choice(loot)
        print("{} acquired.".format(item))
        return item
    else:
        return None


itemDropList = ["biffed boots", "dinky dagger", "shitty shirt", "grimey greaves", "hobo helmet"]
