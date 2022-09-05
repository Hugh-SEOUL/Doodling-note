from tkinter import *

window = Tk()

Label(window,text="너비").grid(row=0)
Label(window,text="높이").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

photo= PhotoImage(file="/phone.jpg")
label =  Label(window, image=photo)
label.grid(row=0)
window.mainloop()

