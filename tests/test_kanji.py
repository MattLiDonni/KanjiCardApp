from PIL import Image, ImageTk
from kanjiapp.kanji import Kanji

def test_kanji():
    kanji = Kanji("雨", "rain", ["ウ"], ["あめ", "あま"], crop=Image.new(mode="RGB", size=(10, 10)))
    assert kanji.character == "雨"

