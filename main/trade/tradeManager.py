# Checks if a trade can be made
def checkTradeAvailable(map, pindex, screenDimensions):
    if map[pindex + 1] in ptrade[0:len(ptrade)] or map[pindex - 1] in ptrade[0:len(ptrade)] or \
            map[pindex - screenDimensions] in ptrade[0:len(ptrade)] or map[pindex + screenDimensions] in ptrade[0:len(ptrade)]:
        return True
    return False


if __name__ == '__main__':
    exit(0)
else:
    ptrade = ['🏠']
