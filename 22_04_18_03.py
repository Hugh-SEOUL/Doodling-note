from tkinter import *

window = Tk()
photo = PhotoImage(file="입벌림방지밴드.png")
l1=Label(window,image=photo).pack(side=RIGHT)
msg = "안녕하세요 삶이 그대를 속일지라도 슬퍼하거나 노여워 하지마라."

l2=Label(window,justify=LEFT, padx=10,text=msg).pack(side=LEFT)

window.mainloop()