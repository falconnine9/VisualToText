import cv2
from math import floor
import time
import os

brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?+-~i!Il;:,^.' "


def videoToText(filename: str, scale: tuple, output):
    frames = ""
    cap = cv2.VideoCapture(filename)
    framerate = None
    shape = [None, None]

    while cap.isOpened():
        if framerate is None:
            framerate = cap.get(cv2.CAP_PROP_FPS)

        ret, frame = cap.read()
        if frame is None:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY, 1)
        frame = cv2.resize(frame, (round(frame.shape[1] / scale[0]), round(frame.shape[0] / scale[1])), cv2.INTER_NEAREST)

        for y in range(frame.shape[0]):
            for x in range(frame.shape[1]):
                pixel = int(frame[y, x])
                frames += brightness[pixel & 0b111111]
            frames += "\n"
        frames += "2"

        if shape[0] is None or shape[1] is None:
            shape[0] = frame.shape[1]
            shape[1] = frame.shape[0]

    cframe = ""
    i = 0
    totaltime = 0
    while i < len(frames)-1:
        starttime = time.time()
        i+=1
        if frames[i] == "2":
            output.write(cframe)
            if (1000 / framerate) - totaltime > 0:
                time.sleep(((1000 / framerate) - totaltime) / 1000)
            cframe = ""
            totaltime = 0
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            cframe += frames[i]
        totaltime += (time.time() - starttime)



