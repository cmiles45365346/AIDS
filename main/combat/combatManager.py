import random


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


def genEnemies(playerx, playery):  # Generates a single enemy around the player when called ignoring all terrain.
    """
    :param playerx: the players x coordinate
    :param playery: the players y coordinate
    :return: nothing yet just appends to a public array
    """
    penemies.append([playerx + random.randint(-32, 32), playery + random.randint(-32, 32), 0, 4, 0])


def moveStraightTowardsPlayer():  # Moves enemy towards player, will add later
    pass


def attackPlayer():  # Enemy attacks the player, will add later
    pass


def renderEnemy(gameMap, screenDimensions, playerx, playery):  # Note does not actually render enemies
    """
    :param gameMap: the world
    :param screenDimensions: the tiles across and down
    :param playerx: the players x coordinate
    :param playery: the players y coordinate
    :return: returns the :param gameMap: with visible enemies overlapped to be handled by the rendering module.
    """

    for enemy in penemies:
        if 0 <= enemy[0] - playerx < 32:
            if 0 <= enemy[1] - playery < 32:
                gameMap[(enemy[0] - playerx) - (playery - enemy[1]) * screenDimensions] = penemy[0]
    return gameMap


if __name__ == '__main__':
    exit(0)
else:  # Variables freely accessible to all methods to edit importing combatManager.
    """
    We could do something cool here where friendlies can become hostile and hostiles can become friendlies.
    """
    penemy = ['E']
    penemies = [[15, 15, 0, 4, 0], [15, 17, 0, 4, 0]]  # x, y, level, xp dropped in death, frames lived
