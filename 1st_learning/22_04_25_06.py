from cgitb import text
from re import T
from tkinter import * 
from tkinter.filedialog import * 

root = Tk()
root.title("파일열기")

root.geometry("400x100")


lbl1 = Label(root, text = "선택된 파일 이름")
lbl1.pack()

filename = askopenfile(root,filetypes=(("GIasdasd","*.gif"),("모든파일","*")))
lbl1.configure(text=str(filename))





root.mainloop()