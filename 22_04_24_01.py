from tkinter import*

window = Tk()

def key(event):
    print(repr(event.char),"가 눌렸씁니다.")

def callback(event):
    frame.focus_set()
    print(event.x,event.y,"에서 마우스 이벤트 발생")
frame = Frame(window,width=200, height=200)
frame.bind("<Key>", key )
frame.bind("<1>",callback)

frame.pack()


window.mainloop()