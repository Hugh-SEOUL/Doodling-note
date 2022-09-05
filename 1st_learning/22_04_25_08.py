from tkinter import * 

top = Tk()
top.title("메모장")
top.geometry("400x400")

ta = Text(top)
sb = Scrollbar(ta)
sb.config(command=ta.yview()) 
sb.pack(side= RIGHT,fill=Y)

top.grid_rowconfigure(0,weight=1)
top.grid_columnconfigure(0,weight=1)

ta.grid(sticky=N+E+S+W)
mb = Menu(top)
fi = Menu(mb, tearoff= 0)
fi.add_command(label="새ㅏㅍ일")
fi.add_command(label="열기")
fi.add_command(label="저장")
fi.add_separator()
fi.add_command(label="종료")

mb.add_cascade(label="파일",menu=fi)
top.config(menu=mb)
END  flie= LEFT
top.mainloop()