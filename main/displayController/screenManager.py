import numpy as np
import cv2


def createBlank(x, y):
    return np.zeros((x, y, 3), np.uint8)


def renderScreen(image, textures, map, x, y):
    return image


def displayScreen(image):
    cv2.imshow("", image)
    cv2.waitKey(1)


if __name__ == '__main__':
    exit(0)
