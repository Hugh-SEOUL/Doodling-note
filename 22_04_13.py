

from tkinter import *

window = Tk()

window.title("배치관리자")

b1 = Button(window, text="버튼1" , width= 80, height= 10 , bg= "blue")
b2 = Button(window, text="버튼2" , width=80, height= 10)

b1.pack(side="left", padx= 20 ,pady= 20)
b2.pack(side="left", padx= 20 ,pady=20 )

b1["text"]= "one"

window.mainloop()