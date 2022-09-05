
from tkinter import *

window = Tk()

t = Text(window,height=2,width=10)
t.pack()

t.insert(END,"텍스트 위젯은 여러줄에\n 텍스를 표시할 수 있다.")
window.mainloop()
