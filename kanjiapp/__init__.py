""" Main application class for Kanji-Card App """
import os
import sys
import time
import logging
from dotenv import load_dotenv
from kanjiapp.gui import GUI
from kanjiapp.util import ImageHandler, Screenshot, ExportDeck
from kanjiapp.kanji import Kanji, KanjiLibrary
from kanjiapp.ocr import KanjiReader
from kanjiapp.dictionary import KanjiLookup

class App:
    """ Main Application """

    def __init__(self):
        load_dotenv()
        os.environ["VERSION"] = "0.1.0"
        
        if not os.getenv("LOG_DIRECTORY"):
            os.environ["LOG_DIRECTORY"] = "."
        logging_level = logging.DEBUG if os.getenv("DEBUG") == "True" else logging.INFO
        logging.basicConfig(level=logging_level, 
                            filename=f"{os.getenv('LOG_DIRECTORY')}/kanjiapp.log", 
                            filemode="w",
                            format="%(asctime)s (%(levelname)s) - %(message)s")
        
        logging.info("Application Started")
        logging.debug("Debug enabled")

        self.gui = GUI()
        self.gui.createLabel(text="Screenshot and select Kanji to export to Anki")
        self.gui.createMenuButton(
            text="Screenshot",
            action=self.screenshotButtonAction,
            bgcolor="OliveDrab1"
        )
        self.gui.createMenuButton(text="Kanji", action=self.kanjiViewerButtonAction)
        self.gui.createMenuButton(text="Export", action=self.exportButtonAction)
        self.gui.createMenuButton(text="Exit", action=self.exitButtonAction)
        self.current_screenshot: Screenshot = None

    def start(self):
        """ Start program execution """
        self.gui.start()

    def finishSelection(self):
        """ Callback function from screenshot-selection window """
        for coordinates in self.current_screenshot.selections:
            try:
                crop = ImageHandler.cropImage(self.current_screenshot.image, *coordinates[0] + coordinates[1])
                character = KanjiReader.read_image(crop)
                KanjiLibrary.add(KanjiLookup.define(character))
            except IndexError:
                logging.warning("Failed to properly read selection.")
            except ValueError:
                logging.warning("No character found in selection.")
        
        print(KanjiLibrary.kanji)
            
            

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

    def kanjiViewerButtonAction(self):
        """ Kanji Viewer Button Event """
        if len(KanjiLibrary.kanji) < 1:
            return self.gui.notify_popup("You haven't screenshotted any characters yet!")
        self.gui.kanjiViewer(title="Current Kanji", onfinish=None)

    def exportButtonAction(self):
        """ Export Button Event """
        export_result = ExportDeck.export(KanjiLibrary.kanji)
        if export_result != True:
            self.gui.notify_popup(export_result)
        else:
            self.gui.notify_popup(title="Success!", message=f"Successfully exported data.")
        

    # button action could be just "exit", but potential future logging/clean up might be needed.
    def exitButtonAction(self):
        """ Exit Button Event """
        sys.exit()
