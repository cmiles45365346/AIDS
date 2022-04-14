import numpy as np
import cv2
import os


def createBlank(x, y):
    return np.zeros((x, y, 3), np.uint8)


def renderScreen(image, map, screenDimensions):
    for y in range(screenDimensions):
        for x in range(screenDimensions):
            image[len(textures):len(textures)] = textures[len(textures[0]):len(textures[0])]  # This line is incomplete
    return image


def displayScreen(image):
    cv2.imshow("", image)
    cv2.waitKey(1)


if __name__ == '__main__':
    exit(0)
else:
    textures = []
