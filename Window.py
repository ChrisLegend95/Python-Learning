import tkinter as tk
import tkinter.ttk as ttk

#--Main window is root. you can name this to what you want it to be defind as or use raw.
root = tk.Tk()

#---geometry is important. This is use to set the size of the window
root.geometry("250x400")

#-- just a title for teh window, it can be anything,
root.title("Tkinter window")

#--(optional) It's not needed if you planing on resize the widnow when it's running. to disable it just put a comment  "#" in teh front of it
root.resizable(0, 0)

#----Buttons! yes buttons is amazing, we can tella button to do anything and this is a simple button i made. you will see more of this down below.

#--ttk is a more modern look while tk is less modern looking. (It's all style of the buttons)

#--In bt you see (root, text="ttk button") root is the window it's sticking to (It's where we telling it what window it goes to) and text is as simple as a Lable, except here we put it in button.
bt = tk.ttk.Button(root, text="ttk button")
#--Note that tk.ttk.button is bind as bt (Button) now you can set this to what you find suting, just remeber if you change the bind you need to do that for everything that use this bind 
#--Place is use to tell the code what pixle this will go in. (Horizontal and vertical offset in pixels)
bt.place(x=50, y=40)

#--Here is a tk button. Looks diffrent from ttk button, but it's still works the same as ttk
bt2 = tk.Button(root, text="tk button")
bt2.place(x=150, y=40)

#---Now Label is as you can guess a text we put in are window, for displaying information, so we know what the program want's or do

#--There is not really much changing of the tk.ttk.Lable and the tk.Lable. you chooses what you want to use
lb = tk.ttk.Label(text="ttk Label")
lb.place(x=50, y=80)

lb2 = tk.Label(text="tk Label")
lb2.place(x=150, y=80)

#--This is a entry and here you can type in words/number ect... in this ent you see (width=10) and this is how long we want teh entry to apper, but you can type out the range of view as well.
ent = tk.ttk.Entry(width=10)
ent.place(x=50, y=100)

#---Difrent here when it's ttk and tk is that tk is more sharp edges adn ttk have rounded edges.

ent2 = tk.Entry(width=10)
ent2.place(x=150, y=100)

#---Radiobuttons. it's what you see normaly when you want to toggle something ona  website or a test online or programs. it's function as a button but got some more activity to it
#---It's a toggle button in short (Radiobutton) it toggle what you what to toggle, as a function or maybe diffrent commands.

rdb = tk.ttk.Radiobutton(text="ttk Radiobutton")
rdb.place(x=20, y=130)

#--- Again, the tk and the ttk have not so big effect here, ttk is nothing more but a modern style to serten props in the window.

rdb2 = tk.Radiobutton(text="tk Radiobutton")
rdb2.place(x=130, y=130)

#--Check buttons are use to show they work diffrent compear to Radiobuttons. Check is a toggle but you can toggle more then 1 at the time. 

ck = tk.ttk.Checkbutton(text="ttk Checkbutton")
ck.place(x=20, y=160)

ck2 = tk.Checkbutton(text="tk Checkbutton")
ck2.place(x=130, y=160)

#---Spinbox is a box you can flip / press a arrow buttin to get the next thing on the list. this can be bind as a selection of nummbers, items, functiosn.

sp = tk.ttk.Spinbox(root, width=12)
sp.place(x=20, y=200)

sp2 = tk.Spinbox(root, width=12)
sp2.place(x=130, y=200)

#---Mainloop is important when it comes to creating a window using tkinter in python. you must have this on the very end for all the widnwos you create. if not you wont get any window poping up.
# it's important to put the bind name of the window you have from root = tk.Tk() so in this case we calling the windwo from top to start the code. "root.mainloop()" this will keep the code in loop for as long until you hit X (closing the window)

root.mainloop()
