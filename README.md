# Upside Down

A little app to flip some image tiles. Inspired by [this tweet](https://twitter.com/humeursdevictor/status/1181919227294433282) from [@humeursdevictor](https://twitter.com/humeursdevictor).

![america]("sample/america.jpg")
![fliped_america]("sample/fliped_america.jpg")

## Build Docker image

`docker build -t upside_down .`

## Run Docker image

`docker container run --rm -$(pwd):/app upside_down <source_image> <destination_image> <tile_shape>`

Where `source_image` is the base image, `destination_image` the path to save the transformed picture and `tile_shape` the size of fliped tile.


