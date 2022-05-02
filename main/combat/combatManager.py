def checkEnemyNearby(gameMap, pindex, screenDimensions):
    if gameMap[pindex + 1] in penemy[0:len(penemy)] or \
            gameMap[pindex - 1] in penemy[0:len(penemy)] or \
            gameMap[pindex - screenDimensions] in penemy[0:len(penemy)] or \
            gameMap[pindex + screenDimensions] in penemy[0:len(penemy)]:
        return True
    return False


def shitCombat(gameMap, pindex, screenDimensions):
    pass


def genEnemies():
    pass


def moveStraightTowardsPlayer():
    pass


def attackPlayer():
    pass


if __name__ == '__main__':
    exit(0)
else:
    penemy = ['E']
