# Upside Down

A little app to flip some image tiles. Inspired by [this tweet](https://twitter.com/humeursdevictor/status/1181919227294433282) from [@humeursdevictor](https://twitter.com/humeursdevictor).

|![america](sample/america.jpg)|![fliped_america](sample/fliped_america.jpg)|
|--|--|

## Build Docker image

`docker build -t upside_down .`

## Run web app

`docker container run --rm -p 8501:8501 upside_down` and open your browser at `0.0.0.0:8501`.
