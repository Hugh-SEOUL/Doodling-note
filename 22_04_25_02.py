from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    root.quit()
    root.destroy() 

root = Tk()
mainmeun = Menu(root)
root.config(menu=mainmeun)

filemenu =Menu(mainmeun, tearoff= 0)
mainmeun.add_cascade(label="파일",menu= filemenu)

filemenu.add_command(label="열기")
filemenu.add_separator()
filemenu.add_command(label="종료")

root.mainloop()