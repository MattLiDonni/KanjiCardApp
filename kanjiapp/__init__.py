""" Main application class for Kanji-Card App """
import os
import sys
import time
from dotenv import load_dotenv
from kanjiapp.gui import GUI
from kanjiapp.util import ImageHandler, Screenshot
from kanjiapp.kanji import Kanji, KanjiLibrary
from kanjiapp.ocr import KanjiReader
from kanjiapp.dictionary import KanjiLookup

class App:
    """ Main Application """

    def __init__(self):
        load_dotenv()
        os.environ["VERSION"] = "0.1.0" # feeling dumb realizing .env for version number doesn't make sense...
        self.gui = GUI()
        self.gui.createLabel(text="Screenshot and select Kanji to export to Anki")
        self.gui.createMenuButton(
            text="Screenshot",
            action=self.screenshotButtonAction,
            bgcolor="OliveDrab1"
        )
        self.gui.createMenuButton(text="Export", action=self.exportButtonAction)
        self.gui.createMenuButton(text="Exit", action=self.exitButtonAction)
        self.current_screenshot: Screenshot
        self.kanji = []

    def start(self):
        """ Start program execution """
        self.gui.start()

    def finishSelection(self):
        """ Callback function from screenshot-selection window """
        for coordinates in self.current_screenshot.selections:
            crop = ImageHandler.cropImage(self.current_screenshot.image, *coordinates[0] + coordinates[1])
            self.kanji.append(KanjiReader.read_image(crop))
        for k in self.kanji:
            print(KanjiLookup.define(k))
        

    ######## Button actions ########
    def screenshotButtonAction(self):
        """
        Screenshot Button Event
        Takes screenshot, then creates second window for screenshot handling."""
        self.gui.minimize()
        time.sleep(0.3)
        self.current_screenshot = Screenshot(ImageHandler.takeScreenshot())
        self.gui.restore()
        self.gui.screenshotEditor(title="Click & Drag to select Kanji", screenshot=self.current_screenshot, onfinish=self.finishSelection)

    def exportButtonAction(self):
        """ Export Button Event """
        print("export")

    # button action could be just "exit", but potential future logging/clean up might be needed.
    def exitButtonAction(self):
        """ Exit Button Event """
        sys.exit()
