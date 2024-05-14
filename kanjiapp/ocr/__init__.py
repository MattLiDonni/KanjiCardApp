import pytesseract
from PIL import Image
import os

class KanjiReader:

    @staticmethod
    def read_image(image: Image):
        """ Read the text from the image and return without whitespace """
        return pytesseract.image_to_string(image, config=os.environ["PYTESSERACT_CONFIG"])\
            .strip().replace('\n', '') # Remove \n for newlines
