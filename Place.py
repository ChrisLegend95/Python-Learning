import tkinter as tk
#---place() Is really accurate and a good way to design and place diffrent tools as a button or text...ect.
#--I personal say that "place()" is mostly for a cleaning up after using "pack()", "grid()". But it's free for you to use how you want.

root = tk.Tk()
root.title("Placing")
root.geometry("350x250")
root.resizable(0, 0)

line1 = tk.Label(text="Hello world.\n This is 100,X and 100,Y using Place")
line1.place(x=100, y=100)
#--Place is use to tell the code what pixle this will go in. (Horizontal and vertical offset in pixels)

button1 = tk.Button(text="x=100, y=50")
button1.place(x=100, y=50)
#--Here Button1 is on 100 Horizontal on pixel and 50 on vertical pixel.

button2 = tk.Button(text="x=190, y=50")
button2.place(x=190, y=50)

root.mainloop()
