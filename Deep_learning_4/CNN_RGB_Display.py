from PIL import Image
import numpy as np

img = Image.open("color.png")
print(img.size)


img = img.resize((28,28))
pixel = np.array(img)

print("Image Info:")
print("Image Shape:",pixel.shape)
print("Height:",pixel.shape[0],"Rows")
print("Weight:",pixel.shape[1],"Weigth")
print("Channels:",pixel.shape[2],"R G B")
total = pixel.shape[0]*pixel.shape[1]*pixel.shape[2]


print("Total Pixel:",total)
print("Single pixel meaning:")
r = pixel[10][10][0]
g = pixel[10][10][1]
b = pixel[10][10][2]

print("Pixel Detail of 10X10 Pixel is:")
print("Red:",r)
print("Green:",g)
print("Blue:",b)
