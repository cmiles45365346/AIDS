def checkEnemyNearby(map, pindex):
    if map[pindex] in penemy[0:len(penemy)]:
        return True
    return False


if __name__ == '__main__':
    exit(0)
else:
    penemy = ['E']
