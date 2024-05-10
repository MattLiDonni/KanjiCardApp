from kanjiapp.util import ImageHandler
from PIL import Image, PngImagePlugin
from kanjiapp.util import ImageHandler

def test_screenshot():
    """ Test if we are getting an Image back """
    assert type(ImageHandler.takeScreenshot()) == Image.Image

def test_crop_image():
    cropped = ImageHandler.cropImage(Image.open("img/screenshot.png", "r", ["PNG"]), 20, 20, 40, 50)
    assert cropped.width == 20 and cropped.height == 30

# Test cropping when not dragging from top-left to bottom-right
def test_crop_bottom_right_to_top_left():
    cropped = ImageHandler.cropImage(Image.open("img/screenshot.png", "r", ["PNG"]), 50, 50, 30, 30)
    assert cropped.width == 20 and cropped.height == 20