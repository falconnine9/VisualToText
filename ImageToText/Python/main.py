import ImageToText

scale = [0, 0]
filename = input("Image file name: ")
scale[0] = float(input("X scale: "))
scale[1] = float(input("Y scale: "))
output_filename = input("Output file name: ")
reverse_brightness = int(input("Reverse brightness scale: "))

with open(output_filename, "w") as f:
    ImageToText.imageToText(filename, tuple(scale), f, reverse_brightness)
