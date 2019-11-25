import tkinter as tk

root = tk.Tk()
root.title("Placing")
root.geometry("350x250")
root.resizable(0, 0)

line1 = tk.Label(text="Hello world.\n This is ... pack")
#---------(By far the best in grid. nothing else is really that good from here.)
line1.grid(column="0", row="0")

button1 = tk.Button(text="pack")
#------------(ipady-x is teh size of teh button. pady-x is teh size of teh background. works porly moving it around)
button1.grid(ipady="10", ipadx="20", pady="20", padx="150")

button2 = tk.Button(text="pack")
#--------------(Sticky is helpful, but not much of free use on the space, column, and row whould fit nice here)
button2.grid(sticky="n")

root.mainloop()