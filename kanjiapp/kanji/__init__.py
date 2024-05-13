from PIL import Image, ImageTk
from typing import List

class Kanji:

    def __init__(self, character: str, meaning: str, onyomi: List[str], kunyomi: List[str], crop:Image=None):
        self.character = character
        self.meaning = meaning
        self.onyomi = onyomi
        self.kunyomi = kunyomi
        self.crop = crop
        self.croptk = ImageTk.PhotoImage(self.crop)
    
    def getImageTk(self) -> ImageTk.PhotoImage:
        return self.croptk

class KanjiLibrary:

    kanji:List[Kanji]

    @classmethod
    def add(cls, kanji: Kanji):
        cls.kanji.append(kanji)