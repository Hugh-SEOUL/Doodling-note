from tkinter import *
from tkinter import *

window = Tk()

canvas = Canvas(window, width=500, height=500, bg= "red")

canvas.pack()

canvas.create_line(0,0,500,500)
canvas.create_line(0,500,500,0,fill="red", width=160)


window.mainloop()