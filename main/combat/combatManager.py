def checkEnemyNearby(map, pindex, screenDimensions):
    if map[pindex + 1] in penemy[0:len(penemy)] or \
            map[pindex - 1] in penemy[0:len(penemy)] or \
            map[pindex - screenDimensions] in penemy[0:len(penemy)] or \
            map[pindex + screenDimensions] in penemy[0:len(penemy)]:
        return True
    return False


if __name__ == '__main__':
    exit(0)
else:
    penemy = ['E']
