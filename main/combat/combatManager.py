def checkEnemyNearby(gameMap, pindex, screenDimensions):
    if gameMap[pindex + 1] in penemy[0:len(penemy)] or \
            gameMap[pindex - 1] in penemy[0:len(penemy)] or \
            gameMap[pindex - screenDimensions] in penemy[0:len(penemy)] or \
            gameMap[pindex + screenDimensions] in penemy[0:len(penemy)]:
        return True
    return False


def badCombat(gameMap, pindex, screenDimensions):  # temporary combat(?)
    print('combat engaged')
    pass


def genEnemies():
    penemies[0] = "E"


def moveStraightTowardsPlayer():
    pass


def attackPlayer():
    pass


def renderEnemy(gameMap, screenDimensions, playerx, playery):
    for enemy in penemies:
        if 0 <= enemy[0] - playerx < 32:
            if 0 <= enemy[1] - playery < 32:
                gameMap[(enemy[0] - playerx) - (playery - enemy[1]) * screenDimensions] = "E"
    return gameMap


if __name__ == '__main__':
    exit(0)
else:
    penemy = ['E']
    penemies = [[15, 15, 0, 4, 0], [15, 16, 0, 4, 0]]  # x, y, level, xp dropped in death, frames lived
