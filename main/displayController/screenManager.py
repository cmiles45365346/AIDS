import numpy as np
import cv2
import os


def createBlank(x, y):  # Returns a black image of size x, y.
    return np.zeros((x, y, 3), np.uint8)


def renderScreen(image, gameMap, screenDimensions):
    for y in range(screenDimensions):
        for x in range(screenDimensions):
            texturesID = 0
            while textures[texturesID] != gameMap[0]:
                texturesID += 2
            image[0:16, 0:16] = textures[texturesID+1][0:16, 0:16]
    return image


def displayScreen(image):
    cv2.imshow("", image)
    cv2.waitKey(1)


if __name__ == '__main__':
    exit(0)
else:
    textures = [" ", cv2.imread("assets/grass.png")]  # Symbol, texture, Symbol, texture...
    image = createBlank(512, 512)
