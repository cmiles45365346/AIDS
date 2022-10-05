import combat.combat_manager as combat
import trade.trade_manager as trade
import inventory.inventory_manager as inventory
import combat.loot_drops as loot
import keyboard
import main

def input_controller(terrain, screen_dimensions, player_collides_with, player_position, player_x, player_y):
    if keyboard.is_pressed("esc"):
        exit("game shut down")
    # Controls in game
    if keyboard.is_pressed("s") and not terrain[player_position + 1] in player_collides_with[0:len(player_collides_with)]:
        player_x += 1
    if keyboard.is_pressed("w") and not terrain[player_position - 1] in player_collides_with[0:len(player_collides_with)]:
        player_x -= 1
    if keyboard.is_pressed("a") and not terrain[player_position - screen_dimensions] in player_collides_with[0:len(player_collides_with)]:
        player_y -= 1
    if keyboard.is_pressed("d") and not terrain[player_position + screen_dimensions] in player_collides_with[0:len(player_collides_with)]:
        player_y += 1
    if keyboard.is_pressed("t"):
        if trade.is_trade_available(terrain, player_position, screen_dimensions):
            # print("Trade can be done")
            trade.sell_item()

        if combat.is_enemy_nearby(terrain, player_position, screen_dimensions):
            # print("Enemy nearby")
            loot.acquire_item()
        # else:
            # print("no enemy nearby")
    if keyboard.is_pressed("e"):  # Opens the inventory so the player can use it.
        # print("inventory should get opened")  # test print
        inventory.player_inventory.open_player_inventory()
        inventory.player_inventory.get_player_gold()
    if keyboard.is_pressed("l"):
        main.server.send_stack.append(["cast_fireball", main.server.public_key])
    return player_x, player_y
