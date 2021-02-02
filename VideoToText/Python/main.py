import VideoToText
import sys

scale = [None, None]
filename = input("Video file name: ")
scale[0] = float(input("X scale: "))
scale[1] = float(input("Y scale: "))

VideoToText.videoToText(filename, tuple(scale), sys.stdout)
