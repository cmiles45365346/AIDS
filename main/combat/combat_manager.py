import random
import inventory.inventory_manager as inventory
import combat.loot_drops as loot


#review time: 1668128107.0732753
def is_enemy_nearby(terrain, player_position, screen_dimensions):  # Checks if an enemy is vertical or horizontal to the player.
    if terrain[player_position + 1] in enemy_symbol[0:len(enemy_symbol)] or \
            terrain[player_position - 1] in enemy_symbol[0:len(enemy_symbol)] or \
            terrain[player_position - screen_dimensions] in enemy_symbol[0:len(enemy_symbol)] or \
            terrain[player_position + screen_dimensions] in enemy_symbol[0:len(enemy_symbol)]:
        return True
    return False


#review time: 1668128107.0732753
def badCombat(terrain, player_position, screen_dimensions):  # temporary combat(?)
    print('combat engaged with enemy!')
    pass


#review time: 1668128107.0732753
def generate_enemy(player_x, player_y):  # Generates a single enemy around the player when called ignoring all terrain.
    enemies.append([player_x + random.randint(-8, 8) + 16, player_y + random.randint(-8, 8) + 15])
    return enemies


#review time: 1668128107.0732753
def move_straight_towards_player():  # Moves enemy towards player, will add later
    pass


#review time: 1668128107.0732753
def npc_attack_player():  # Enemy attacks the player, will add later
    pass


#review time: 1668128107.0732753
def render_enemies(terrain, screen_dimensions, player_x, player_y):  # Note does not actually render enemies
    for enemy in enemies:
        if 0 <= enemy[0] - player_x < 32:
            if 0 <= enemy[1] - player_y < 32:
                terrain[(enemy[0] - player_x) - (player_y - enemy[1]) * screen_dimensions] = enemy_symbol[0]
    return terrain


#review time: 1668128107.0732753
def render_players(terrain, screen_dimensions, player_x, player_y, players):  # Note does not actually render players
    for player in players:
        if 0 <= player[0] - player_x < 32:
            if 0 <= player[1] - player_y < 32:
                terrain[(player[0] - player_x) - (player_y - player[1]) * screen_dimensions] = player_symbol[0]
    return terrain


if __name__ == '__main__':
    exit(0)
else:  # Variables freely accessible to all methods to edit importing combatManager.
    
    # We could do something cool here where friendlies can become hostile and hostiles can become friendlies.
    enemy_symbol = ['E']
    player_symbol = ['A']
    
    # Below to be moved to server
    enemies = []  # type x, y, level, xp dropped in death, frames lived
