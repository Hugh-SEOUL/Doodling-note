from tkinter import*


class CANVAS_SHAPE:
    def __init__(self):
        window = Tk()
        window.title("여러가지 도형 그리기")
        
        self.canvas = Canvas(window,width=600,height=400, bg= "white")
        self.canvas.pack()
        
        frame = Frame(window, bg="black",width=600,height=100)
        frame.pack()

        btnrectangle = Button(frame, text="사각형",command=self.displayrect)
        btnoval = Button(frame,text="원그리기",command=self.displayoval)
        btnarc = Button(frame,text="아크그리기",command=self.displayrc)
        btnpolygon = Button(frame,text="다각그리기",command=self.displaypolygon)
        btnline = Button(frame,text="선그리기",command=self.displayline)

        window.mainloop()
        
        
if __name__ == "__main__":
    CANVAS_SHAPE()