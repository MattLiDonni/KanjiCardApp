""" Simpler functions that are easier to seperate to prevent cluttering other classes """
import pyautogui
from PIL import Image, ImageTk
from typing import List

class Screenshot:

    def __init__(self, image:Image):
        self.image = image
        self.imagetk = ImageTk.PhotoImage(image=self.image)
        self.selections: List[tuple] = []

    def getImageTk(self) -> ImageTk.PhotoImage:
        return self.imagetk

    def addSelection(self, x0:int, y0:int, x1:int, y1:int) -> bool:
        coordinates = ImageHandler.coordinate_correction(x0, y0, x1, y1)
        self.selections.append(coordinates)
        return True
    
    def getSelections(self) -> List[tuple]:
        return self.selections

    def popSelection(self) -> tuple:
        return self.selections.pop()


class ImageHandler:
    """ Handles screenshotting and images """
    @staticmethod
    def takeScreenshot() -> Image.Image:
        img = pyautogui.screenshot()
        print(type(img))
        return img

    @staticmethod
    def coordinate_correction(x0:int, y0:int, x1:int, y1:int) -> tuple:
        top_left = [x0, y0]
        bottom_right = [x1, y1]

        if x0 > x1:
            top_left[0] = x1
            bottom_right[0] = x0
        if y0 > y1:
            top_left[1] = y1
            bottom_right[1] = y0
        return top_left, bottom_right

    @staticmethod
    def cropImage(image: Image, x0:int, y0:int, x1:int, y1:int) -> Image:
        top_left, bottom_right = ImageHandler.coordinate_correction(x0, y0, x1, y1)
        try:
            return image.crop(top_left + bottom_right)
        except ValueError:
            return 0

class MouseHandler:
    
    @classmethod
    def leftClick(cls, event):
        cls.button1_down = True
        print("LeftClick - " + str(event.x) + ", " + str(event.y))
        return event.x, event.y

    @classmethod
    def release(cls, event):
        cls.button1_down = False
        print("Released - " + str(event.x) + ", " + str(event.y))
        return event.x, event.y

    @classmethod
    def mouseMotion(cls, event):
        if cls.button1_down:
            return event.x, event.y
        return None
