import numpy
import cv2


def flip_image_tiles(image, tile_shape):
    image = cv2.imdecode(numpy.frombuffer(image.read(), numpy.uint8), 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    fliped_tiles = []
    for row in range(0, image.shape[0], tile_shape):
        for col in range(0, image.shape[1], tile_shape):
            tile = image[row:row + tile_shape, col:col + tile_shape, :]
            fliped_tile = numpy.flip(tile, (0,1))  # only flip x and y axis
            image[row:row + tile_shape, col:col + tile_shape, :] = fliped_tile
    return image
