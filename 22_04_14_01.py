from cgitb import text
from tkinter import *


window = Tk()

frame = Frame(window)
b1 = Button(frame, text= "박스 1", bg="red", fg="white").pack(side="left")
b2 = Button(frame, text= "박스 2", bg="green", fg="white").pack(side="left")
b3 = Button(frame, text= "박스 3", bg="orange", fg="white").pack(side="left")
label= Label(window,text= "이 레이블은 버튼 ㅇ ㅟ에 배치")
label.pack()
frame.pack()

window.mainloop()
  