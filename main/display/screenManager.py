import numpy as np
import cv2
import os


def createBlank(x, y):  # Returns a black image of size x, y.
    return np.zeros((x, y, 3), np.uint8)


def renderScreen(image, gameMap, screenDimensions):  # Renders onto the blank screen.
    for y in range(screenDimensions):
        for x in range(screenDimensions):
            texturesID = 0
            try:
                while textures[texturesID] != gameMap[x + (y * screenDimensions)]:
                    texturesID += 2
            except Exception as e:
                exit("Cannot render object onto the screen in screenManager unknown symbol")
            image[0 + x * 16:16 + x * 16, 0 + y * 16:16 + y * 16] = textures[texturesID + 1][0:16, 0:16]
    return image


def resizeScreen(image):
    return cv2.resize(image, (768, 768))


def displayScreen(image):
    cv2.imshow("", image)
    cv2.waitKey(1)


if __name__ == '__main__':
    exit(0)
else:
    # Warning game cannot render objects outside of range and will crash in such a scenario
    textures = [  # assign symbol to image
        "8", cv2.imread("assets/grassUp.png"),
        "6", cv2.imread("assets/grassRight.png"),
        "2", cv2.imread("assets/grassDown.png"),
        "4", cv2.imread("assets/grassLeft.png"),
        "∧", cv2.imread("assets/mountain.png"),  # ∧ is mountain symbol not ^ comparison ∧^ we will change this later.
        "🏠", cv2.imread("assets/trader.png"),
        "A", cv2.imread("assets/player.png"),
        "a", cv2.imread("assets/trader.png"),
        "E", cv2.imread("assets/enemy.png")
    ]  # Symbol, texture,
    image = createBlank(512, 512)
