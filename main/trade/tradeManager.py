# Checks if a trade can be made
def checkTradeAvailable(gameMap, pindex, screenDimensions):
    if gameMap[pindex + 1] in ptrade[0:len(ptrade)] or \
            gameMap[pindex - 1] in ptrade[0:len(ptrade)] or \
            gameMap[pindex - screenDimensions] in ptrade[0:len(ptrade)] or \
            gameMap[pindex + screenDimensions] in ptrade[0:len(ptrade)]:
        return True
    return False


if __name__ == '__main__':
    exit(0)
else:
    ptrade = ['🏠']
