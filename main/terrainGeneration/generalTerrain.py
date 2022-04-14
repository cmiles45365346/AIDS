# map generated is 32*32
import random


def ran():
    return random.randint(1, 5000)  # Generates pseudo random number between 1 and 5000 for generation


# Generates cells in square area offset by player position
# This could be improved by generating only cells that are needed offset by player position when missing. 
def generateCells(screenx, screeny):
    map = []  # Start with blank map
    for x in range(32):
        for y in range(32):
            # Get seed for cell in a real game might want to pass the number output as a md5 hash to make it more
            # unpredictable.
            random.seed(x + screenx + ((y + screeny) * 32))
            randnum = ran()  # generate cell number based off seed used

            if x + screenx > 5000 or x + screenx < -5000 or y + screeny < -5000 or y + screeny > 5000:  # World border, 5000 is world borders size in a direction
                map.append("∧")
            elif randnum < 4900:
                map.append(" ")
            elif randnum < 4982:
                map.append("∧")
            elif randnum < 5001:
                map.append("🏠")
            elif randnum < 4991:
                map.append("")

            else:
                map.append("~")
    return map  # Returns generated map as output
