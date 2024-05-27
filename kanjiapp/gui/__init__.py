""" GUI for Kanji App, contains GUI functions and some other things that should be seperated in the future """

from tkinter import Tk, Label, Button, Misc, Image, Toplevel, Canvas, NW
from PIL import ImageTk
from PIL import Image as IM
import os
from kanjiapp.util import MouseHandler, ImageHandler, Screenshot
from kanjiapp.kanji import Kanji, KanjiLibrary

class GUI(Tk):
    """ Extends Tk() from tkinter, adds custom functionality for Kanji App """

    def __init__(self) -> None:
        """ Creates main application window """
        super().__init__()
        self.title("Kanji To Anki v" + os.environ["VERSION"])
        geometry = "600x200+" + str(int(self.winfo_screenwidth()/3))\
            + "+" + str(int(self.winfo_screenheight()/3))
        self.geometry(geometry)
        self.components = []
        self.screenshot: Screenshot

        # For Canvas
        self.rects = []
        self.drawingRect:int = None
        self.mouseStartPos = tuple()
        self.mouseCurrentPos = tuple()
        self.mouseReleasePos = tuple()
        self.onfinish:callable = None

    def start(self) -> None:
        """ Start the GUI """
        self.mainloop()

    #### Widgets ####
     
    def createLabel(self, master:Misc=None, text:str="Label") -> None: # Will be changed later
        """ Creates a label widget """
        if master == None:
            master = self
        label = Label(master=master,
            text=text,
            wraplength=400)
        label.pack(side="left", fill="both")
        self.components.append(label)

    def createMenuButton(self,
                         master:Misc=None,
                         text:str="Button",
                         action:callable=None,
                         bgcolor:str="ivory2"
                         ) -> None:
        """ Creates a label widget """
        if master == None:
            master = self
        button = Button(master=self,
                text=text,
                command=action,
                bg=bgcolor)
        button.pack(fill="both", expand=True)
        self.components.append(button)

    # TODO Create a general "secondary window" object
    def screenshotEditor(self, screenshot: Screenshot, master:Misc=None, title:str="Secondary Window", fullscreen:bool=True, onfinish:callable=None):
        """ Creates another window for editing/selecting from screenshots """
        self.screenshot = screenshot
        self.screenshotWindow = Toplevel(master=self)
        self.screenshotWindow.title(title)
        self.onfinish = onfinish
        self.canvas = Canvas(master=self.screenshotWindow, width=self.screenshot.image.width, height=self.screenshot.image.height, bd=0, highlightthickness=0)
        self.canvas.pack_propagate(False)
        Label(master=self.canvas, text="Click and drag with Mouse 1 to select.\nUndo with Mouse 2\n Esc to finish").pack(side='top')
        self.canvas.pack(padx=0, pady=0, ipadx=0, ipady=0)
        self.canvas.create_image(0,0,anchor=NW,image=self.screenshot.getImageTk())
        self.screenshotWindow.focus_set()

        # Mouse Binds
        # TODO VVV have these defined outside of GUI maybe, and make these point to those functions VVV
        self.screenshotWindow.bind("<ButtonPress-1>", self.leftClick)
        self.screenshotWindow.bind("<ButtonPress-3>", self.rightClick)
        self.screenshotWindow.bind("<ButtonRelease-1>", self.release)
        self.screenshotWindow.bind("<B1-Motion>", self.motion)
        self.screenshotWindow.bind("<Escape>", self.esc)

        self.screenshotWindow.attributes("-fullscreen", True)

    def kanjiViewer(self, master:Misc=None, title:str="Secondary Window", onfinish:callable=None):
        try:
            self.kanjiwindow.destroy()
        except AttributeError:
            pass
        self.kanjiwindow = Toplevel(master=self)
        self.kanjiwindow.title(title)
        self.onfinish = onfinish
        self.kanjiwindow.geometry(f"800x500+{str(int(self.winfo_screenwidth()/3)-100)}+{str(int(self.winfo_screenheight()/3)-100)}")

        if len(KanjiLibrary.kanji) == 0: Label(master=self.kanjiwindow, text="You don't have any characters defined yet!").pack(side="top")
        else: Label(master=self.kanjiwindow, text="Click on an item to delete it from the current list").pack(side="top")

        for character in KanjiLibrary.kanji:
            KanjiListItem(master=self.kanjiwindow, character=character).pack()

        Button(master=self.kanjiwindow, text="Exit", command=self.kanjiwindow.destroy, width=10, height=3).pack(side="bottom")


    # Mouse bind events

    def leftClick(self, event):
        self.mouseStartPos = MouseHandler.leftClick(event)

    def rightClick(self, event):
        print(self.rects)
        if len(self.rects) > 0:
            self.canvas.delete(self.rects.pop())
            self.screenshot.popSelection()

    def release(self, event):
        if self.drawingRect:
            self.canvas.delete(self.drawingRect)
            self.drawingRect = None
        self.mouseReleasePos = MouseHandler.release(event)
        if self.mouseStartPos[0] != self.mouseReleasePos[0] and self.mouseStartPos[1] != self.mouseReleasePos[1]: # if its not a box then dont save it.
            self.rects.append(self.canvas.create_rectangle(self.mouseStartPos, self.mouseReleasePos, fill='', outline="#00ffff", width=2))
            self.screenshot.addSelection(*self.mouseStartPos + self.mouseReleasePos)

    def motion(self, event):
        if self.drawingRect:
            self.canvas.delete(self.drawingRect)
        self.mouseCurrentPos = MouseHandler.mouseMotion(event)
        self.drawingRect = self.canvas.create_rectangle(self.mouseStartPos, self.mouseCurrentPos, fill='', outline="#00ffff", width=2)

    def esc(self, event):
        self.screenshotWindow.attributes("-fullscreen", False)
        
        # Reset all values
        self.rects = []
        self.drawingRect = None
        self.mouseStartPos = tuple()
        self.mouseCurrentPos = tuple()
        self.mouseReleasePos = tuple()
        # Destroy window
        self.screenshotWindow.destroy()
        self.screenshotWindow = None
        self.onfinish()

    #### Functionality ####

    def minimize(self):
        """ Minimize window to taskbar """
        self.iconify()

    def restore(self):
        """ Restore minimized window """
        self.deiconify()


class KanjiListItem(Button):

    def __init__(self, master, character):
        super().__init__(master=master, text=KanjiLibrary.kanji[character], command=self.onClick, font=("Arial", 16))
        self.character = character
    
    def onClick(self):
        KanjiLibrary.delete(self.character)
        self.destroy()
        
