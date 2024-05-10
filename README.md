## My Still-Unnamed Kanji App v0.1 - Matthew LiDonni

### This is a small Python application that (when finished) will allow a user to take a screenshot of their display and pick out Kanji characters to add to an Anki flashcard deck for studying.

I've started recently learning Japanese, and the one issue I've had was forcing myself to make flashcards. Kanji are logographic characters, and not only are they crucial to reading Japanese, but there's around 2000 of them that are commonly taught and considered important for daily use.
It's exhaustive, and even if writing them does help with memorizing them, I figured it would be much more fun to turn into this project.
If you're reading something online, or playing a visual novel, and you come across a Kanji you don't know, you can just have this program open on the side, press screenshot, select the Kanji or Vocab, get the definition so you can keep reading, and later when you want to study you've got it already in an Anki deck.

The ideal steps of this programs usage would be
Main Menu > Screenshot > Window opens > Select Kanji > Press Finish > Automatically looks up and fills in Kanji information > Open selected Kanji menu and look over all characters > Press export > Open Anki > Import Deck > Import the exported file

### Features so far:

- Simple tkinter GUI
- Screenshot display
- Click and drag selection of Kanji (Similar to rectangle select in Snipping Tool)
  - Click and drag to select characters, right click to undo
  - Saves to a folder 'img' at run location, but currently deletes previous selection)

### Features needed to be considered finished:

- .env file with configurations
- Improve Image Handling
  - Current implementation is for testing, saves over images
- OCR character recognition
  - PyTesseract, currently working in a version on the side but yet to be integrated
- Dictionary lookup for Meanings, Vocab, Onyomi/Kunyomi readings, and any other information
  - JamDict works well, uses JMDict which I originally planned to download and use before finding it.
- Export Kanji to file for Anki flashcard deck
- Interactable menu of currently selected Kanji
- Logging

### Potential features after being finished:

- Settings menu
- Selected Kanji menu additions
  - Option to view the cropped image to compare to what the OCR returned
  - Add Kanji manually that autofill with information.
- Edit information returned by JamDict.
- Edit raw version of export file before exporting
- Web version?
- Train and use my own image-recognition model based on Kuzushiji-Kanji dataset or Kuzushiji-MNIST dataset
  - Scary, this is a far-future goal.
- More things I cannot remember currently, but will update when I do.

Please read before using:
I am not liable for anything that breaks, including any lost files or damage that this may cause on your device. I'm designing it as a side project, and it will probably have some bugs and issues for a little while. By using this software, you acknowledge that you understand this, and that this software is being developed purely for fun, and using it is at your own risk.

### To use:

- Pull repo
- Create virtual environment
- Enable virtual environment
- Install requirements from requirements.txt
- run main.py
