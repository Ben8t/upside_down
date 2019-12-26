"""main.py"""
import argparse
import numpy
import cv2
import io
from src.utils import flip_image_tiles

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Upside Down images.")
    arg_parser.add_argument("original_image", help="Original image file path.")
    arg_parser.add_argument("destination_image", help="Transformerd image file path.")
    arg_parser.add_argument("tile_shape", type=int, help="Tile shape (will be a square)")
    args = arg_parser.parse_args()

    with open(args.original_image, "rb") as image_stream:
        image_buffer = io.BytesIO(image_stream.read())
        fliped_image = flip_image_tiles(image_buffer, args.tile_shape)

    image_to_write = cv2.cvtColor(fliped_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(args.destination_image, image_to_write)

