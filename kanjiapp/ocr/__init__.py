import pytesseract
from PIL import Image
import os

class KanjiReader:

    @staticmethod
    def read_image(image: Image):
        return pytesseract.image_to_string(image, config=os.environ["PYTESSERACT_CONFIG"]).strip('\n')
