from pyvirtualdisplay import Display
from kanjiapp import App

def test_virtual_display():
    with Display(visible=False, size=(100, 60)) as disp:
        assert disp.is_alive()

def test_app_init():
    with Display(visible=False, size=(100, 60)) as disp:
        assert App()
