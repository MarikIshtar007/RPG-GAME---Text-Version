from tkinter import *
import os
from time import sleep
from PIL import ImageTk, Image

root=Tk()
root.geometry("700x600+200+10")
root.config(bg="#778899")
root.resizable(0,0)

insertion_idx = 1.0

# Narration Texts and Dialogues
intro = ["Welcome to the Fire and Shadow. An exicitng text-based RPG- Game.\n",
"In this game you will be assuming the role of a 17 year-old prince,\n",
"locked in his own castle's dungeon after the attack of a neighbouring Kingdom.\n",
"You were knocked unconscious, and now wake up in the dungeon.\n",
"Help guide the prince to his freedom\n",
"And reclaim your rightful throne!!\n"
]

# Loading all image assets
logo = ImageTk.PhotoImage(Image.open(r"assets\images\logo.png"))

# Logo Widget
canvas=Canvas(root,bg="blue" ,height=250, width=420)
canvas.grid(row=0,column=1,padx=140,pady=20)
canvas.create_image(-30, -20,anchor=NW, image = logo)


# Output Text Widget
text_out=Text(root,height=14,width=82,bg="black", fg="white", insertbackground="white", wrap=WORD)
text_out.place(x=20, y=290)
# text_out.configure(state='disabled')

# Input Text Widget
text_in=Text(root, height=2, width=82, bg="white")
text_in.place(x=20, y=540)

# Helper Functions
def send(output):
    global insertion_idx
    text_out.configure(state='normal')
    text_out.insert(str(insertion_idx), output)
    insertion_idx+=len(output)
    text_out.configure(state='disabled')

'''def send_loop(output):
    global insertion_idx
    text_out.insert(str(insertion_idx), output)
    insertion_idx+=len(output)'''

def slow_output(output_list,i):
	global insertion_idx
	if i<len(output_list):
		text_out.configure(state='normal')
		text_out.insert(insertion_idx,output_list[i])
		insertion_idx+=len(output_list[i])
		text_out.configure(state='disabled')
		text_out.after(1200,lambda: slow_output(output_list,i+1))
	else:
		pass
    


# Core Logic
slow_output(intro,0)

# Main Application Loop
root.mainloop()
