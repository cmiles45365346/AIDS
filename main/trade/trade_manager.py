import inventory.inventory_manager as inventory
import combat.loot_drops as loot

# Checks if a trade can be made
#review time: 1668264674.6824646
def is_trade_available(terrain, player_position, screen_dimensions):
    if terrain[player_position + 1] in trader[0:len(trader)] or \
            terrain[player_position - 1] in trader[0:len(trader)] or \
            terrain[player_position - screen_dimensions] in trader[0:len(trader)] or \
            terrain[player_position + screen_dimensions] in trader[0:len(trader)]:
        return True
    return False

#review time: 1668264674.6824646
def sell_item():
    # print(inventory.PlayerInventory.inventory.index(loot.itemDropList[0])) # prints the index number of item 0
    if loot.item_drops[0] in inventory.player_inventory.inventory:
        selling = inventory.player_inventory.inventory.index(loot.item_drops[0])
        inventory.player_inventory.inventory.pop(selling)
        inventory.player_inventory.inventory[0] += 5
        print("sold, +5 gold")
    else:
        print("No {} in inventory.".format(loot.item_drops[0]))
    pass


if __name__ == '__main__':
    exit(0)
else:
    trader = ['a']
