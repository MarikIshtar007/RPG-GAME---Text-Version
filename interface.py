from tkinter import *

root=Tk()
root.geometry("700x600+200+10")
root.config(bg="yellow")

canvas=Canvas(root,bg="blue",height=200,width=300)
canvas.grid(row=0,column=1,padx=200,pady=20)

text_out=Text(root,height=14,width=82,bg="white")
text_out.place(x=20,y=290)

text_in=Text(root,height=2,width=82,bg="white")
text_in.place(x=20,y=540)

root.mainloop()