from tkinter import *
from tkinter import font
class APP:
    def __init__(self):
        root = Tk()
        self.customFont = font.Font(family="Helvetica",size= 12)
        buttonframe = Frame()
        label = Label(root, text= "hello world",font=self.customFont)
        buttonframe.pack() 
        label.pack()

        bigger = Button(root,text="텍ㄱ스트를 작게", command= self.bigFont)
        smaller = Button(root, text="크게",command= self.smallFont)
        bigger.pack()
        smaller.pack()
        
        root.mainloop()
    def bigFont(self):
        size = self.customFont["size"]
        print(size)
        self.customFont.config(size= size+2)
        print(self.customFont)
        
    def smallFont(self):
        size = self.customFont["size"]
        print(size)
        self.customFont.config(size= size-2)
        print(self.customFont)
        
        
if __name__ == "__main__":
    APP()
