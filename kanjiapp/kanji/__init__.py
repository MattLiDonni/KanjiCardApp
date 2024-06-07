from PIL import Image, ImageTk
from typing import List

class Kanji:

    def __init__(self, character:str, meanings:List[str]=None, readings:List[str]=None, crop:Image=None):
        self.character = character
        self.meanings = meanings
        self.readings = readings
        self.crop = crop
    
    def getImageTk(self) -> ImageTk.PhotoImage:
        """ Return the image as an ImageTk object """
        if self.crop:
            return ImageTk.PhotoImage(self.crop)
        raise ValueError("Kanji has no defined image to pull from!")
    
    def __repr__(self):
        return f"Kanji({self.character}, {self.meanings}, {self.readings}, {self.crop}"

class KanjiLibrary:

    kanji: dict[str, Kanji] = {}

    @classmethod
    def add(cls, kanji: Kanji):
        """ Add a kanji to the current list """
        cls.kanji[kanji.character] = kanji

    @classmethod
    def delete(cls, character: str):
        """ Delete a stored kanji """
        cls.kanji.pop(character)
        print("Deleted " + character)
