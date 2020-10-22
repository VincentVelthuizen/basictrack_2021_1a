from PIL import Image
import numpy as np

im = Image.open("brightened.png")
pix = np.array(im)

shift = np.min(pix)    # make sure the lowest number is 0
scale = 255 / (np.max(pix) - np.min(pix))     # and the highest will be 255

# create a new list for the new image
new_pix = []
for row in pix:
    new_row = []
    for pixel in row:
        new_row.append((pixel - shift) * scale)
    new_pix.append(new_row)

new_pix = np.array(new_pix).astype('uint8')
im2 = Image.fromarray(new_pix)
# show the new image
im2.show()
