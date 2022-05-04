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
    pass


def moveStraightTowardsPlayer():
    pass


def attackPlayer():
    pass


def renderEnemy(gameMap, screenDimensions):
    return gameMap



if __name__ == '__main__':
    exit(0)
else:
    penemy = ['E']
    penemies = []
