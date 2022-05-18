# map generated is to dimensionSize in main
import random


def ran():
    return random.randint(1, 5000)  # Generates pseudo random number between 1 and 5000 for generation


# Generates cells in square area offset by player position
# This could be improved by generating only cells that are needed offset by player position when missing. 
def generateCells(screenx, screeny, screenDimensions):
    gameMap = []  # Start with blank map
    for x in range(screenDimensions):
        for y in range(screenDimensions):
            # Get seed for cell in a real game might want to pass the number output as a md5 hash to make it more
            # unpredictable.
            random.seed(x + screenx + ((y + screeny) * screenDimensions))
            randnum = ran()  # generate cell number based off seed used

            if x + screenx > 5000 or x + screenx < -5000 or y + screeny < -5000 or y + screeny > 5000:  # World border, 5000 is world borders size in a direction
                gameMap.append("∧")
            elif randnum < 1235:  # generates upwards grass tile
                gameMap.append("8")
            elif randnum < 2470:  # generates right grass tiles
                gameMap.append("6")
            elif randnum < 3705:  # generates down grass tile
                gameMap.append("2")
            elif randnum < 4940:  # generates left grass tile
                gameMap.append("4")

            elif randnum < 4982:  # generates mountains
                gameMap.append("∧")
            elif randnum < 5001:  # generates traders
                gameMap.append("a")
            else:
                gameMap.append("~")
    return gameMap  # Returns generated map as output


def renderOverlay(gameMap, screenDimensions, playerx, playery):
    """
    :param gameMap: the world
    :param screenDimensions: the tiles across and down
    :param playerx: the players x coordinate
    :param playery: the players y coordinate
    :return: returns the :param gameMap: with visible enemies overlapped to be handled by the rendering module.
    """

    for x in range(screenDimensions):
        for y in range(screenDimensions):
            pass
    return gameMap

"""
    for enemy in penemies:
        if 0 <= enemy[0] - playerx < 32:
            if 0 <= enemy[1] - playery < 32:
                gameMap[(enemy[0] - playerx) - (playery - enemy[1]) * screenDimensions] = penemy[0]
    return gameMap
"""

if __name__ == '__main__':
    terrain = []
    exit(0)
