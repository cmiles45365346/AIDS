import inventory.inventory_manager as inventory
import secrets

#review time: 1668264737.4451013
def acquire_item():
    inventory.player_inventory.inventory[0] += 10  # you get 10 pennies for combat, subject to change, prob should be random but seed go brr
    dropped_item = choose_random_item(item_drops)
    if dropped_item != None:  # if an item is acquired and is call
        inventory.player_inventory.inventory.append(dropped_item)

#review time: 1668264737.4451013
def choose_random_item(loot):
    if secrets.choice(range(0, 3)) == 0:  # 1/3 Chance to get an item
        dropped_item = secrets.choice(loot)
        print("{} acquired.".format(dropped_item))
        return dropped_item
    return None


item_drops = ["biffed boots", "dinky dagger", "shitty shirt", "grimey greaves", "hobo helmet"]
