
from tkinter import *





window = Tk()
def show():
    print("이름: {}\n나이: {}".format(e1.get(), e2.get()))

Label(window, text="이름").grid(row=0)
Label(window, text="이름").grid(row=1)


e1 = Entry(window)
e2= Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window,text="종료",command= window.quit).grid(row=2,column=0,sticky= W , pady=5)
Button(window,text="보이기",command= show).grid(row=2,column=1,sticky= W,pady=5)



window.mainloop()

