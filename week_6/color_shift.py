from PIL import Image
import numpy as np

# open the image to be accessed using 'im'
im = Image.open("fruit_fade_2.png")
# convert the image to a numpy array called 'pix'
pix = np.array(im)

# create a new list for the new image
new_pix = []
for row in pix:
    # create a new list for each row of pixels in the image
    new_row = []
    for pixel in row:
        # add each converted pixel (here +100) to the new row
        new_row.append(pixel + 100)
        # should make sure the new numbers are in range...
    # add the new row to the new image
    new_pix.append(new_row)

# convert the new image to an array of 8 bit integers
# uint8 => unsigned (no negative numbers) integers of 8 bits
new_pix = np.array(new_pix).astype('uint8')
# convert the array into an image
im2 = Image.fromarray(new_pix)
# show the new image
# im2.show()
im2.save("fruit_fade_2.png")
