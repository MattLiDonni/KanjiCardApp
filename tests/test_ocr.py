from PIL import Image
from kanjiapp.ocr import KanjiReader

'''
def test_read_image():
    """ If changing the tested text/image, beware that the space is the one used on the JP keyboard"""
    image = Image.open("tests/test_data/sekai_konnichiwa.png")
    assert KanjiReader.read_image(image) == "世界、 こんにちは" # Hello world in Japanese
    image.close()
'''