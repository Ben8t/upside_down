"""main.py"""
import argparse
import numpy
import cv2

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Upside Down images.")
    arg_parser.add_argument("original_image", help="Original image file path.")
    arg_parser.add_argument("destination_image", help="Transformerd image file path.")
    arg_parser.add_argument("tile_shape", type=int, help="Tile shape (will be a square)")
    args = arg_parser.parse_args()
    tile_shape = args.tile_shape

    image = cv2.imread(args.original_image)
    fliped_tiles = []
    for row in range(0, image.shape[0], tile_shape):
        for col in range(0, image.shape[1], tile_shape):
            tile = image[row:row + tile_shape, col:col + tile_shape, :]
            fliped_tile = numpy.flip(tile, (0,1))  # only flip x and y axis
            image[row:row + tile_shape, col:col + tile_shape, :] = fliped_tile

    cv2.imwrite(args.destination_image, image)
