import tkinter as tk
#--The buttons are Lable with "anchor" and "side". just so it's easier to see what is what in the code and the window.
root = tk.Tk()
root.title("Placing")
root.geometry("350x250")
root.resizable(0, 0)

line1 = tk.Label(text="Hello world.\n This is ... pack")
#--This "pack()" manager organizes widgets in blocks before placing them in the parent widget
#--So your Lable/Buttons is using blocks of the window size to place and fitt them nice and orginiced for you. it's a simple way to place button and text fast to see fast result.
line1.pack()

button1 = tk.Button(text="anchor")
button1.pack(anchor="nw")
#-Anchors are used to define where text is positioned relative to a reference point.
#-you can use following "NW" "N" "NE" "W" "CENTER" "E" "SW" "S" "SE"
#-It is as i call it teh compass format and it use that "N" is north wish is on teh bottom of window and "s" is top of the window

button2 = tk.Button(text="side")
button2.pack(side="bottom")
#-(side="bottom") Determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT.

root.mainloop()
