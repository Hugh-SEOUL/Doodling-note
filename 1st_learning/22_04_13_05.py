from tkinter import *

window = Tk()

class APP:
    def __init__(self):
        window = Tk()
        helloB= Button(window,text = "hello", command=self.hello, fg= "red")
        helloB.pack(side="left")
        quitB = Button(window,text="quit",command=self.quit)
        quitB.pack(side="left")
        window.mainloop()

    def hello(self):
        print("헬로우 버튼이 클릭")
    def quit(self):
        print("퀴트 버튼이 클릭")


APP()        