from pyvirtualdisplay import Display
import os
from kanjiapp import App

def test_virtual_display():
    os.environ['DISPLAY'] = ':0'
    with Display(visible=False, size=(100, 60), use_xauth=True) as disp:

        assert disp.is_alive()

def test_app_init():
    os.environ['DISPLAY'] = ':0'
    with Display(visible=False, size=(100, 60), use_xauth=True) as disp:
        assert App()
