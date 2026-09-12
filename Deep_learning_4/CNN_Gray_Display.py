from PIL import Image
import numpy as np

img = Image.open("digit_28X28.png")

img = img.convert("L")

img = img.resize((28,28))

pixel = np.array(img)
print("Image Size :",pixel.shape)

print("Pixel Values:")
print(pixel)

#	0 =>	Black
#	255 =>	White
#	50 => 	Gray
#	120 => 	med Gray
#	200 => Lite Gray

