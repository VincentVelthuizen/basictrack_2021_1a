from PIL import Image
import numpy as np


def fade_bw(image):
    pixels = np.array(image, dtype='uint8')
    new_pix = [[(sum(pixels[row, col]) / 7) for col in range(pixels.shape[1])] for row in range(pixels.shape[0])]
    new_image = Image.fromarray(np.array(new_pix, dtype='uint8'))
    new_image.show()

    return new_image


def fade_color(image):
    pixels = np.array(image, dtype='int8')

    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            pixels[row, col, 0] *= 0.5
            pixels[row, col, 1] *= 0.5
            pixels[row, col, 2] *= 0.5

    new_image = Image.fromarray(pixels)
    new_image.show()

    return new_image


if __name__ == "__main__":
    im = Image.open("fruit.jpg")
    im2 = fade_bw(im)
    im2.save("fruit_fade.png", "PNG")
