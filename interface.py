from tkinter import *
import os
from time import sleep
from PIL import ImageTk, Image

root=Tk()
root.geometry("800x600+200+10")
root.config(bg="#778899")
root.resizable(0,0)

insertion_idx = 1.0

# Narration Texts and Dialogues

intro = [
["Welcome to the Fire and Shadow. An exicitng text-based RPG- Game.\n\n","narration"],
["In this game you will be assuming the role of a 17 year-old prince,\n", "narration"],
["locked in his own castle's dungeon after the attack of a neighbouring Kingdom.\n", "narration"],
["You were knocked unconscious, and now wake up in the dungeon.\n", "narration"],
["Help guide the prince to his freedom\n","narration"],
["And reclaim your rightful throne!!\n", "narration"]
]

name=[["What would you like to name your character?\n", "narration"]]

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

def initialize_colors():
	text_out.tag_configure("narration", foreground="yellow")
	text_out.tag_configure("mc", foreground="#0000F0")



def slow_output(output_list,i=0):
	btn.configure(state='disabled')
	global insertion_idx
	if i<len(output_list):
		text_out.configure(state='normal')
		text_out.insert(insertion_idx,output_list[i][0], output_list[i][1])
		insertion_idx+=len(output_list[i][0])
		text_out.configure(state='disabled')
		text_out.after(1200,lambda: slow_output(output_list,i+1))
	else:
		pass
	btn.configure(state='normal')

def intro_done():
	clear_output()
	next = "level0"
	print(name[0][0], name[0][1])
	slow_output(name)


# Loading all image assets
logo = ImageTk.PhotoImage(Image.open(r"assets\images\logo.png"))

# Logo Widget
canvas=Canvas(root,bg="blue" ,height=200, width=336)
canvas.grid(row=0,column=1,padx=140,pady=20)
canvas.create_image(-30, -20,anchor=NW, image = logo)


# Output Text Widget
text_out=Text(root,height=18,width=95,bg="LightBlue4", fg="white", insertbackground="white", wrap=WORD)
text_out.place(x=18, y=240)
scroll = Scrollbar(root ,command =text_out.yview)
scroll.place(x=763,y=242,height=288)
text_out.configure(yscrollcommand=scroll.set)
text_out.configure(state='disabled')

# Input Text Widget
text_in=Text(root, height=2, width=85, bg="#58737b")
text_in.place(x=17, y=540)

# The Button
btn_text="Next"
btn_command = intro_done
btn = Button(root,text=btn_text,command = btn_command, bg="grey",fg="white", font=("Sans Serif",11,"bold"), height = 1, padx= 15, pady=3)
btn.place(x=710, y = 540)

def clear_output():
	global insertion_idx
	insertion_idx = 1.0
	text_out.delete(1.0, END)
	text_out.update()
# Core Logic
initialize_colors()
slow_output(intro)

# Main Application Loop
root.mainloop()

