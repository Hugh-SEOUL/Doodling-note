from html import entities
import re
from tkinter import*

from random import * 


answer = randint(1,100)

def guessing():
    guess = int(guessfield.get())
    if guess > answer:
        msg = "높음!"
    elif guess < answer:
        msg = "낮음!"
    else:
        msg = "정답!"
    
    resultlabel["text"] = msg
    guessfield.delete(0,5)
    
def resett():
    global answer
    answer = randint(1,100)
    resultlabel["text"]= "다시한번도전하세요"

window = Tk()
window.configure(bg="blue") 
window.title("숫자추측게임")
window.geometry("900x80")

titlelabel = Label(window, text="숫자게임에 오신것을 환영")
titlelabel.pack()

guessfield = Entry(window)
guessfield.pack(side=LEFT,padx= 100)

trybutton = Button(window,text="시도",fg="green",bg="white", command= guessing)
resetbutton = Button(window,text="초기화",fg="red", command= resett)
trybutton.pack(side=LEFT,padx=15)
resetbutton.pack(side=LEFT,padx=15)

resultlabel = Label(window,text="1부터 100사이의 숫자를 입력하세요",bg="green")
resultlabel.pack(side=LEFT)

window.mainloop()