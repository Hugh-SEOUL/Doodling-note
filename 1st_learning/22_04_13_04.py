
from cgitb import text
from tkinter import *

window = Tk()

# def callaback():
#     b1["text"]= "버튼이 클릭되었슴"

# b1 = Button(window, text="클릭", command= callaback)

# b1.pack(side="left")
# window.mainloop()

count = 0

def clicked():
    global count
    count += 1
    label["text"] = "버튼클릭횟수:", str(count)
    return count
if __name__== "__main__":
    label =Label(window,text="아직 클릭되지 않았슴")
    label.pack()
    b1 = Button(window, text="증가", command= clicked)
    b2 = Button(window, text="리셋", command= clicked)
    b1.pack()
    b2.pack()
    
    window.mainloop()
    
    def reset():
        