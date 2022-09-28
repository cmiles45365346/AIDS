import random
import inventory.inventoryManager as inventory
import combat.lootDrops as loot


def checkEnemyNearby(gameMap, pindex, screenDimensions):  # Checks if an enemy is vertical or horizontal to the player.
    """
    :param gameMap: the world
    :param pindex: the location of the player on the game map
    :param screenDimensions: the tiles across and down
    :return: true if an object in penemies array is
    """
    if gameMap[pindex + 1] in penemy[0:len(penemy)] or \
            gameMap[pindex - 1] in penemy[0:len(penemy)] or \
            gameMap[pindex - screenDimensions] in penemy[0:len(penemy)] or \
            gameMap[pindex + screenDimensions] in penemy[0:len(penemy)]:
        return True
    return False


def badCombat(gameMap, pindex, screenDimensions):  # temporary combat(?)
    """
    :param gameMap: the world
    :param pindex: the location of the player on the game map
    :param screenDimensions: the tiles across and down
    :return: nothing yet
    """
    print('combat engaged with enemy!')
    pass


def gen_enemies(player_x, player_y):  # Generates a single enemy around the player when called ignoring all terrain.
    """
    Generates 2 enemies
    :param player_x: the players x coordinate
    :param player_y: the players y coordinate
    :return: nothing yet just appends to a public array
    """
    penemies.append([player_x + random.randint(-32, 32), player_y + random.randint(-32, 32), 0, 4, 0])
    return penemies


def moveStraightTowardsPlayer():  # Moves enemy towards player, will add later
    pass


def attackPlayer():  # Enemy attacks the player, will add later
    pass


def render_enemy(game_map, screen_dimensions, player_x, player_y):  # Note does not actually render enemies
    """
    Overlay enemies on the game_map
    :param game_map: The worlds map
    :param screen_dimensions: Array of the tiles across and down
    :param player_x: the players x coordinate
    :param player_y: the players y coordinate
    :return: returns the :param gameMap: with visible enemies overlapped to be handled by the rendering module.
    """

    for enemy in penemies:
        if 0 <= enemy[0] - player_x < 32:
            if 0 <= enemy[1] - player_y < 32:
                game_map[(enemy[0] - player_x) - (player_y - enemy[1]) * screen_dimensions] = penemy[0]
    return game_map


def render_players(game_map, screen_dimensions, player_x, player_y):
    """
    Overlay enemies on the game_map
    :param game_map: The worlds map
    :param screen_dimensions: Array of the tiles across and down
    :param player_x: the players x coordinate
    :param player_y: the players y coordinate
    :return: returns the :param gameMap: with visible players overlapped to be handled by the rendering module.
    """
    for player in players:
        if 0 <= player[0] - player_x < 32:
            if 0 <= player[1] - player_y < 32:
                game_map[(player[0] - player_x) - (player_y - player[1]) * screen_dimensions] = pplayer[0]
    return game_map


if __name__ == '__main__':
    exit(0)
else:  # Variables freely accessible to all methods to edit importing combatManager.
    # We could do something cool here where friendlies can become hostile and hostiles can become friendlies.
    penemy = ['E']
    pplayer = ['P']
    penemies = [[15, 15, 0, 4, 0], [15, 17, 0, 4, 0]]  # type x, y, level, xp dropped in death, frames lived
    players = []
