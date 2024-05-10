""" GUI for Kanji App, contains GUI functions and some other things that should be seperated in the future """

from tkinter import Tk, Label, Button, Misc, Image, Toplevel, Canvas, NW
from PIL import ImageTk
from PIL import Image as IM
import os
from kanjiapp.util import MouseHandler, ImageHandler

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

        # For Canvas
        self.rects = []
        self.drawingRect:int = None
        self.mouseStartPos = tuple()
        self.mouseCurrentPos = tuple()
        self.mouseReleasePos = tuple()

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

    def screenshotEditor(self, image=Image, master:Misc=None, title:str="Secondary Window", fullscreen:bool=True):
        """ Creates another window for editing/selecting from screenshots """
        self.screenshotWindow = Toplevel(master=self)
        self.screenshotWindow.title(title)
        self.image = image # Need to save both parts of the image or it will not work
        self.imagetk = ImageTk.PhotoImage(image=self.image)
        self.canvas = Canvas(master=self.screenshotWindow, width=self.image.width, height=self.image.height, bd=0, highlightthickness=0)
        self.canvas.pack(padx=0, pady=0, ipadx=0, ipady=0)
        self.canvas.create_image(0,0,anchor=NW,image=self.imagetk)

        # Mouse Binds
        self.screenshotWindow.bind("<ButtonPress-1>", self.leftClick)
        self.screenshotWindow.bind("<ButtonPress-3>", self.rightClick)
        self.screenshotWindow.bind("<ButtonRelease-1>", self.release)
        self.screenshotWindow.bind("<B1-Motion>", self.motion)

        
        self.screenshotWindow.attributes("-fullscreen", True)


    # Mouse bind events

    def leftClick(self, event):
        self.mouseStartPos = MouseHandler.leftClick(event)

    def rightClick(self, event):
        print(self.rects)
        if len(self.rects) > 0:
            self.canvas.delete(self.rects.pop())

    def release(self, event):
        if self.drawingRect:
            self.canvas.delete(self.drawingRect)
            self.drawingRect = None
        self.mouseReleasePos = MouseHandler.release(event)
        self.rects.append(self.canvas.create_rectangle(self.mouseStartPos, self.mouseReleasePos, fill='', outline="#00ffff", width=2))
        # TODO Replace with screenshot image
        ImageHandler.cropImage(IM.open("img/screenshot.png", "r", ["PNG"]), *self.mouseStartPos + self.mouseReleasePos).save("img/crop.png")

    def motion(self, event):
        if self.drawingRect:
            self.canvas.delete(self.drawingRect)
        self.mouseCurrentPos = MouseHandler.mouseMotion(event)
        self.drawingRect = self.canvas.create_rectangle(self.mouseStartPos, self.mouseCurrentPos, fill='', outline="#00ffff", width=2)
    #### Functionality ####

    def minimize(self):
        """ Minimize window to taskbar """
        self.iconify()

    def restore(self):
        """ Restore minimized window """
        self.deiconify()
