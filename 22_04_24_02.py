from tkinter import*

window = Tk()

def left(event):
    print("단일 클릭,왼쪽버튼")
def double_click(event):
    print("더블 클릭,왼쪽버튼")
        
        
button = Button(None, text= "마우스 클릭")

button.bind("<Button-1>", left)
button.bind("<Double-1>", double_click)

button.pack()
button.mainloop()