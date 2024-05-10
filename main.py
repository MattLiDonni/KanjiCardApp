""" Entry point for the Kanji Application """
import os
from kanjiapp import App

if __name__ == "__main__":
    if not os.getenv('DISPLAY'): 
        # prevents pyautogui errors in github actions, normally set by your OS
        os.environ['DISPLAY'] = ':0'
    App().start()
