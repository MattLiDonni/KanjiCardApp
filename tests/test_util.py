from kanjiapp.util import ImageHandler
from PIL import Image, PngImagePlugin
from kanjiapp.util import ImageHandler, Screenshot
"""
def test_screenshot_object():
    screenshot = Screenshot(Image.new("RGB", (10, 10)))
    assert screenshot

def test_screenshot_selection():
    screenshot = Screenshot(Image.new("RGB", (10, 10)))
    assert screenshot.addSelection(2, 2, 6, 6)
    
def test_screenshot_pop():
    screenshot = Screenshot(Image.new("RGB", (10, 10)))
    screenshot.addSelection(2, 2, 6, 6)
    screenshot.popSelection()
    assert len(screenshot.selections) == 0

def test_crop_image():
    cropped = ImageHandler.cropImage(Image.new("RGB", (10, 10)), 0, 0, 6, 6)
    assert cropped.width == 6 and cropped.height == 6

# Test cropping when not dragging from top-left to bottom-right
def test_crop_bottom_right_to_top_left():
    cropped = ImageHandler.cropImage(Image.new("RGB", (10, 10)), 6, 6, 0, 0)
    assert cropped.width == 6 and cropped.height == 6

"""