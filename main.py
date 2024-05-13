""" Entry point for the Kanji Application """
import os
from kanjiapp import App

if __name__ == "__main__":
    if not os.getenv('DISPLAY'): 
        # Supposed to prevent pyautogui errors in github actions, but doesnt. 
        # is normally set by your OS. Needs to be fixed.
        os.environ['DISPLAY'] = ':0'
    App().start()
