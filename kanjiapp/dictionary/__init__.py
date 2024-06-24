from jamdict import Jamdict
from kanjiapp.kanji import Kanji

class KanjiLookup:
    jam = Jamdict()

    @classmethod
    def define(cls, text:str) -> Kanji:
        result = cls.jam.lookup(text)
        kanji = Kanji(character=text)

        readings = []
        for reading in result.entries:
            readings.append(reading.kana_forms)

        kanji.meanings = result.chars[0].meanings(english_only=True)
        kanji.readings = readings[0]

        return kanji