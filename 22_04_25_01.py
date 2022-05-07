from tkinter import * 
from tkinter.colorchooser import askcolor
from unittest.mock import DEFAULT

DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = "BLACK"

mode = "pen"
old_X = None
old_y = None
mycolor = DEFAULT_COLOR
erase_on = False

def use_pen():
    global mode
    mode = "pen"

def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)[1]
    print("변경된 생삭 :",mycolor)
    
def use_erase():
    global mode
    mode = "erase"

def paint(event):
    