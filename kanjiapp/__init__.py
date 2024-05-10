""" Main application class for Kanji-Card App """
import os
import sys
import time
from kanjiapp.gui import GUI
from kanjiapp.util import ImageHandler

class App:
    """ Main Application """

    def __init__(self):
        os.environ["VERSION"] = "0.1.0" # will use dotenv for a config file in the near future
        self.gui = GUI()
        self.gui.createLabel(text="Screenshot and select Kanji to export to Anki")
        self.gui.createMenuButton(
            text="Screenshot",
            action=self.screenshotButtonAction,
            bgcolor="OliveDrab1"
        )
        self.gui.createMenuButton(text="Export", action=self.exportButtonAction)
        self.gui.createMenuButton(text="Exit", action=self.exitButtonAction)
        self.img = None

    def start(self):
        """ Start program execution """
        self.gui.start()

    ######## Button actions ########
    def screenshotButtonAction(self):
        """
        Screenshot Button Event
        Takes screenshot, then creates second window for screenshot handling."""
        self.gui.minimize()
        time.sleep(0.3)
        self.img = ImageHandler.takeScreenshot()
        self.gui.restore()
        self.gui.screenshotEditor(title="Click & Drag to select Kanji", image=self.img)

    def exportButtonAction(self):
        """ Export Button Event """
        print("export")

    # button action could be just "exit", but potential future logging/clean up might be needed.
    def exitButtonAction(self):
        """ Exit Button Event """
        sys.exit()
