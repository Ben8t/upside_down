import streamlit
from src.utils import flip_image_tiles


streamlit.title("Upside Down")

tile_shape = streamlit.sidebar.slider("Tile size", 0, 100, 25, 5)

source_image = streamlit.sidebar.file_uploader("Source image", ["png", "jpg", "jpeg"]) 


if source_image is not None:
    fliped_image = flip_image_tiles(source_image, tile_shape)
    streamlit.image(fliped_image)


if streamlit.sidebar.button("Show source image"):
    streamlit.image(source_image)
