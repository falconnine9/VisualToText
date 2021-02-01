import cv2
from math import floor

brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?+-~i!Il;:,^.' "


def imageToText(filename: str, scale: tuple, output, reverse_brightness = 0):
    if reverse_brightness == 1:
        global brightness
        brightness = brightness[::-1]
    img = cv2.imread(filename, 0)
    if img is None:
        return -1

    img = cv2.resize(img, (int(img.shape[1] / scale[0]), int(img.shape[0] / scale[1])))

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            pixel = int(img[y, x])
            output.write(brightness[floor(pixel * (len(brightness) / 255)) - 1])
        output.write("\n")

    return 0
