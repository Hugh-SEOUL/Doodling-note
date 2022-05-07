from tkinter import * 
from tkinter.filedialog import * 

root = Tk()
root.title("파일저장")

root.geometry("400x100")

lbl1 = Label(root, text="저장된 파일이름")
lbl1.pack()

savefb = asksaveasfile(parent=root,mode="w", defaultextension=".jpg" , filetypes=(("jpg","*.jpg"),("모든파일","*.*")))

lbl1.configure(text=savefb)
savefb.close()

root.mainloop()