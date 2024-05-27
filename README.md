## My Still-Unnamed Kanji App v0.1 - Matthew LiDonni

### This is a small Python application that (when finished) will allow a user to take a screenshot of their display and pick out Kanji characters to add to an Anki flashcard deck for studying.

I've started recently learning Japanese, and the one issue I've had was forcing myself to make flashcards. Kanji are logographic characters, and not only are they crucial to reading Japanese, but there's around 2000 of them that are commonly taught and considered important for daily use.
It's exhaustive, and even if writing them does help with memorizing them, I figured it would be much more fun to turn into this project.
If you're reading something online, or playing a visual novel, and you come across a Kanji you don't know, you can just have this program open on the side, press screenshot, select the Kanji or Vocab, get the definition so you can keep reading, and later when you want to study you've got it already in an Anki deck.

The ideal steps of this programs usage would be
Main Menu > Screenshot > Window opens > Select Kanji > Press Finish > Automatically looks up and fills in Kanji information > Open selected Kanji menu and look over all characters > Press export > Open Anki > Import Deck > Import the exported file

### Current Issues:

- Tests are failing in Github Actions since a virtual display is needed for many functionalities, testing currently with pyvirtualdisplay
  - Currently put off to work on other features, will possibly change existing features to allow testing without the need for a virtual display.

### Feature progress:

- Simple tkinter GUI (Done, needs overhaul in near future)
- Screenshot and display on a window (Done)
- Click and drag selection of Kanji (Similar to rectangle select in Snipping Tool)
  - Click and drag to select characters, right click to undo
- OCR character recognition (PyTesseract)
- Dictionary lookup for Meanings, readings (JamDict)

### Features needed to be considered finished:

- Flesh out .env file with configurations
- Add related vocab
- Export Kanji to file for Anki flashcard deck
- Interactable menu of currently selected Kanji
- Logging

### Potential features after being finished:

- Visual overhaul
- Settings menu
- Selected Kanji menu additions
  - Option to view the cropped image to compare to what the OCR returned
  - Add Kanji manually that autofill with information.
- Edit information returned by JamDict.
- Edit raw version of export file before exporting
- Web version?
- Train and use my own image-recognition model based on Kuzushiji-Kanji dataset or Kuzushiji-MNIST dataset
  - Scary, this is a far-future goal.

Please read before using:
I am not liable for anything that breaks, including any lost files or damage that this may cause on your device. I'm designing it as a side project, and it will probably have some bugs and issues for a little while. By using this software, you acknowledge that you understand this, and that this software is being developed purely for fun, and using it is at your own risk.

### To use:

Windows:

- Clone repo `git clone https://github.com/MattLiDonni/KanjiCardApp`
- Create virtual environment `python -m venv venv`
- Enable virtual environment `venv/Scripts/activate`
- Install wheel `pip install wheel`
- Install requirements from requirements.txt `pip install -r requirements.txt`
- run main.py `python main.py`
