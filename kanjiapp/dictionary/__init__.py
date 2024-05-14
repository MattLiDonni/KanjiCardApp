from jamdict import Jamdict

class KanjiLookup:
    jam = Jamdict()

    @classmethod
    def define(cls, text:str):
        return cls.jam.lookup(text) # TODO change return