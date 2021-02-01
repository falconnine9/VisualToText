import ImageToText

scale = [0, 0]
filename = input("Image file name: ")
scale[0] = int(input("X scale: "))
scale[1] = int(input("Y scale: "))
output_filename = input("Output file name: ")
reverse_brightness = int(input("Reverse brightness scale: "))

with open(output_filename, "w") as f:
    ImageToText.imageToText(filename, tuple(scale), f, reverse_brightness)
