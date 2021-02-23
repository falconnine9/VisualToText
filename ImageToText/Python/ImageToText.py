import cv2
from math import floor

brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?+-~i!Il;:,^.' "


def imageToText(filename: str, scale: tuple, output):
    img = cv2.imread(filename, 0)
    if img is None:
        return

    img = cv2.resize(img, (int(img.shape[1] / scale[0]), int(img.shape[0] / scale[1])))

    output_str = ""
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            pixel = int(img[y, x])
            output_str += brightness[pixel & 0b111111]
        output_str += "\n"

    output.write(output_str)
